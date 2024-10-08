import io

import requests
import weasyprint
from capeditor.cap_settings import CapSetting
from capeditor.renderers import CapXMLRenderer
from django.conf import settings
from django.core.files.base import ContentFile
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext as _
from lxml import etree
from wagtail.api.v2.utils import get_full_url
from wagtail.documents import get_document_model
from wagtail.images import get_image_model
from wagtail.models import Site

from climweb.base.models import ImportantPages
from climweb.base.weasyprint_utils import django_url_fetcher
from .constants import DEFAULT_STYLE, CAP_LAYERS
from .sign import sign_cap_xml


def get_all_published_alerts():
    from .models import CapAlertPage
    return CapAlertPage.objects.all().live().filter(status="Actual", scope="Public").order_by('-sent')


def get_currently_active_alerts():
    current_time = timezone.localtime()
    return get_all_published_alerts().filter(expires__gte=current_time)


def create_cap_geomanager_dataset(cap_geomanager_settings, has_live_alerts, request=None):
    sub_category = cap_geomanager_settings.geomanager_subcategory

    more_info = None

    if request:
        important_pages = ImportantPages.for_request(request)
        if important_pages.cap_warnings_list_page:
            more_info = {
                "linkText": _("Go to warnings list"),
                "linkUrl": important_pages.cap_warnings_list_page.get_full_url(request),
                "isButton": True,
                "showArrow": True
            }

    if not sub_category:
        return None

    title = cap_geomanager_settings.layer_title
    metadata = cap_geomanager_settings.geomanager_layer_metadata
    auto_refresh_interval = cap_geomanager_settings.auto_refresh_interval

    # convert to milliseconds
    if auto_refresh_interval:
        auto_refresh_interval = auto_refresh_interval * 60 * 1000

    cap_geojson_url = cap_geomanager_settings.get_cap_geojson_url(request)

    dataset_id = "cap_alerts"

    dataset = {
        "id": dataset_id,
        "dataset": dataset_id,
        "name": title,
        "isCapAlert": True,
        "capConfig": {
            "baseUrl": cap_geojson_url,
            "refreshInterval": auto_refresh_interval
        },
        "initialVisible": has_live_alerts,
        "layer": dataset_id,
        "category": sub_category.category.pk,
        "sub_category": sub_category.pk,
        "public": True,
        "layers": []
    }

    if metadata:
        dataset.update({"metadata": metadata.pk})

    layer = {
        "id": dataset_id,
        "dataset": dataset_id,
        "name": title,
        "layerConfig": {
            "type": "vector",
            "source": {
                "type": "geojson",
                "data": {"type": "FeatureCollection", "features": []},
            },
            "render": {
                "layers": CAP_LAYERS
            },
        },
        "layerFilterParams": {
            "severity": [
                {"label": "Extreme", "value": "Extreme"},
                {"label": "Severe", "value": "Severe"},
                {"label": "Moderate", "value": "Moderate"},
                {"label": "Minor", "value": "Minor"},
            ],
        },
        "layerFilterParamsConfig": [
            {
                "isMulti": True,
                "type": "checkbox",
                "key": "severity",
                "required": "true",
                "default": [
                    {"label": "Extreme", "value": "Extreme"},
                    {"label": "Severe", "value": "Severe"},
                    {"label": "Moderate", "value": "Moderate"},
                ],
                "sentence": "Filter by Severity {selector}",
                "options": [
                    {"label": "Extreme", "value": "Extreme"},
                    {"label": "Severe", "value": "Severe"},
                    {"label": "Moderate", "value": "Moderate"},
                    {"label": "Minor", "value": "Minor"},
                    {"label": "Unknown", "value": "Unknown"},
                ],
            },
        ],
        "legendConfig": {
            "items": [
                {
                    "color": "#d72f2a",
                    "name": "Extreme Severity",
                },
                {
                    "color": "#fe9900",
                    "name": "Severe Severity",
                },
                {
                    "color": "#ffff00",
                    "name": "Moderate Severity",
                },
                {
                    "color": "#03ffff",
                    "name": "Minor Severity",
                },
                {
                    "color": "#3366ff",
                    "name": "Unknown Severity",
                },
            ],
            "type": "basic",
        },
        "interactionConfig": {
            "capAlert": True,
            "type": "intersection",
        },
    }

    if more_info:
        layer["moreInfo"] = more_info

    dataset["layers"].append(layer)

    return dataset


def create_cap_pdf_document(cap_alert, template_name):
    site = Site.objects.get(is_default_site=True)
    cap_settings = CapSetting.for_site(site)

    # TODO: handle case where logo is not set
    org_logo = cap_settings.logo

    html_string = render_to_string(template_name, {
        'page': cap_alert,
        "org_logo": org_logo,
        "sender_name": cap_settings.sender_name,
        "sender_contact": cap_settings.sender,
        "alerts_url": cap_alert.get_parent().get_full_url().strip("/"),
    })

    html = weasyprint.HTML(string=html_string, url_fetcher=django_url_fetcher, base_url='file://')

    buffer = io.BytesIO()
    html.write_pdf(buffer)

    buff_val = buffer.getvalue()

    content_file = ContentFile(buff_val, f"{cap_alert.identifier}.pdf")

    document = get_document_model().objects.create(title=cap_alert.title, file=content_file)

    return document


def get_cap_map_style(geojson):
    style = DEFAULT_STYLE
    style["sources"].update({"cap_alert": {"type": "geojson", "data": geojson}})
    layers = CAP_LAYERS
    for layer in layers:
        layer_type = layer.get("type")
        layer["source"] = "cap_alert"

        if layer_type == "fill":
            layer["id"] = "cap_alert_fill"

        if layer_type == "line":
            layer["id"] = "cap_alert_line"

        if layer.get("filter"):
            del layer["filter"]

    style["layers"].extend(layers)

    return style


def create_cap_area_map_image(cap_alert):
    MBGL_RENDERER_URL = getattr(settings, "MBGL_RENDERER_URL", None)

    if not MBGL_RENDERER_URL:
        print("MBGL_RENDERER_URL is not set in settings")
        return None

    mbgl_payload = cap_alert.mbgl_renderer_payload

    headers = {'Content-type': 'application/json'}
    r = requests.post(MBGL_RENDERER_URL, data=mbgl_payload, headers=headers, stream=True)

    r.raise_for_status()

    file_id = cap_alert.last_published_at.strftime("%s")
    filename = f"{cap_alert.identifier}_{file_id}_map.png"

    sent = cap_alert.sent.strftime("%Y-%m-%d-%H-%M")
    image_title = f"{sent} - Alert Area Map"

    # create content file from response
    content_file = ContentFile(r.content, filename)
    area_image = get_image_model().objects.create(title=image_title, file=content_file)

    return area_image


def get_cap_settings():
    site = Site.objects.get(is_default_site=True)
    cap_settings = CapSetting.for_site(site)
    return cap_settings


def format_date_to_oid(date):
    # Extract date components
    year = date.year
    month = date.month
    day = date.day
    hour = date.hour
    minute = date.minute
    second = date.second

    # Format components into OID
    oid_date = f"{year}.{month}.{day}.{hour}.{minute}.{second}"

    return oid_date


def serialize_and_sign_cap_alert(alert, request=None):
    from .serializers import AlertSerializer

    data = AlertSerializer(alert, context={
        "request": request,
    }).data

    xml = CapXMLRenderer().render(data)
    xml_bytes = bytes(xml, encoding='utf-8')
    signed = False

    try:
        signed_xml = sign_cap_xml(xml_bytes)
        if signed_xml:
            xml = signed_xml
            signed = True
    except Exception as e:
        pass

    if signed:
        root = etree.fromstring(xml)
    else:
        root = etree.fromstring(xml_bytes)

    style_url = get_full_url(request, reverse("cap_alert_stylesheet"))

    tree = etree.ElementTree(root)
    pi = etree.ProcessingInstruction('xml-stylesheet', f'type="text/xsl" href="{style_url}"')
    tree.getroot().addprevious(pi)
    xml = etree.tostring(tree, xml_declaration=True, encoding='utf-8')

    return xml, signed
