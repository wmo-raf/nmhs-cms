from typing import Any, Dict, List

from capeditor.models import CapSetting
from capeditor.renderers import CapXMLRenderer
from capeditor.serializers import AlertSerializer
from django.contrib.syndication.views import Feed
from django.db.models.base import Model
from django.http import JsonResponse
from django.urls import reverse
from django.utils import timezone
from django.utils.feedgenerator import Enclosure
from django.utils.feedgenerator import Rss201rev2Feed
from rest_framework import generics
from wagtail.models import Site

from .models import CapAlertPage


class CustomFeed(Rss201rev2Feed):
    content_type = 'application/xml'

    def add_item_elements(self, handler, item):
        super().add_item_elements(handler, item)
        if item['author_name']:
            handler.addQuickElement('author', item['author_name'])


class AlertListFeed(Feed):
    link = "/rss.xml"
    feed_copyright = "public domain"
    language = "en"

    feed_type = CustomFeed

    def title(self):
        try:
            site = Site.objects.get(is_default_site=True)
            if site:
                cap_setting = CapSetting.for_site(site)
                return f"Latest Official Public alerts from {cap_setting.sender_name}"

        except Exception:
            pass

        else:
            return "Latest Official Public alerts"

        return None

    def description(self):

        try:
            site = Site.objects.get(is_default_site=True)
            if site:
                cap_setting = CapSetting.for_site(site)

                return f"This feed lists the most recent Official Public alerts from {cap_setting.sender_name}"

        except Exception:
            pass

        else:
            return "This feed lists the most recent Official Public alerts"

        return None

    def items(self):
        alerts = CapAlertPage.objects.all().live().filter(status="Actual")
        return alerts

    def item_title(self, item):
        return item.title

    def item_link(self, item):
        return reverse("cap_alert_detail", args=[item.identifier])

    def item_description(self, item):
        return item.info[0].value.get('description')

    def item_pubdate(self, item):
        return item.sent

    def item_enclosures(self, item: Model) -> List[Enclosure]:
        return super().item_enclosures(item)

    def item_guid(self, item):
        return item.identifier

    def item_author_name(self, item):
        try:
            site = Site.objects.get(is_default_site=True)
            if site:
                cap_setting = CapSetting.for_site(site)
                return cap_setting.sender

        except Exception:
            pass

        else:
            return item.sender

        return None

    def item_extra_kwargs(self, item: Model) -> Dict[Any, Any]:
        return {
            "category": item.info[0].value.get('category')
        }

    def item_categories(self, item):
        return [item.info[0].value.get('category')]


class AlertDetail(generics.RetrieveAPIView):
    serializer_class = AlertSerializer
    serializer_class.Meta.model = CapAlertPage

    renderer_classes = (CapXMLRenderer,)
    queryset = CapAlertPage.objects.live().filter(status="Actual")

    lookup_field = "identifier"


def cap_geojson(request):
    alerts = CapAlertPage.objects.all().live().filter(status="Actual")
    active_alert_infos = []

    for alert in alerts:
        for info in alert.info:
            if info.value.get('expires') > timezone.localtime():
                active_alert_infos.append(alert.id)

    active_alerts = CapAlertPage.objects.filter(id__in=active_alert_infos).live()

    geojson = {
        "type": "FeatureCollection",
        "features": []
    }

    for active_alert in active_alerts:
        features = active_alert.get_geojson_features(request)
        if features:
            geojson["features"].extend(features)

    return JsonResponse(geojson)
