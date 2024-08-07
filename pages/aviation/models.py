import uuid
from django.contrib.gis.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from wagtail.api.v2.utils import get_full_url

from wagtailgeowidget.helpers import geosgeometry_str_to_struct
from wagtailgeowidget.panels import LeafletPanel, GeoAddressPanel
from wagtail_color_panel.edit_handlers import NativeColorPanel

from django_extensions.db.fields import AutoSlugField
from wagtailgeowidget import geocoders
from wagtail_color_panel.fields import ColorField
from wagtail.snippets.models import register_snippet
from wagtail.admin.panels import FieldPanel
from base.mixins import MetadataPageMixin
from wagtail.models import Page

from wagtail.contrib.routable_page.models import RoutablePageMixin
from django.utils import timezone
from adminboundarymanager.models import AdminBoundarySettings

class AirportCategory(models.Model):
    name = models.CharField(_("Category name"), max_length=50)
    color = ColorField(blank=True, null=True, default="#363636",
                               help_text=_("Category color"))
    
    panels = [
        FieldPanel('name'),
        NativeColorPanel('color')
    ]
    class Meta:
        verbose_name = _("Airport Category")
        verbose_name_plural = _("Airport Categories")


    def __str__(self) -> str:
        return self.name

# Create your models here.
class Airport(models.Model):
    id = models.CharField(unique=True, primary_key=True,)
    name = models.CharField(verbose_name=_("Airport Name"), max_length=255, null=True, blank=False, unique=True)
    slug = AutoSlugField(populate_from='name', null=True, unique=True, default=None, editable=False)
    category = models.ForeignKey(AirportCategory, verbose_name=_("Airport Category"), on_delete=models.CASCADE)
    location = models.PointField(verbose_name=_("Airport Location (Lat, Lng)"))
    
    
    panels = [
        FieldPanel("id"),
        GeoAddressPanel("name", geocoder=geocoders.NOMINATIM),
        FieldPanel("category"),
        LeafletPanel("location", address_field="name"),
    ]

    class Meta:
        verbose_name = _("Airport")
        verbose_name_plural = _("Airports")
        ordering = ['name']

    def __str__(self):
        return self.name

    @property
    def coordinates(self):
        location = geosgeometry_str_to_struct(str(self.location))
        return [float(location['x']), float(location['y'])]

    @property
    def x(self):
        return self.coordinates[0]

    @property
    def y(self):
        return self.coordinates[1]
    
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        airport_search_url = get_full_url(request, reverse("airports-list"))
        context.update({
            "airports_search_url": airport_search_url,
        })

        return context



class Message(models.Model):

    MSG_FORMAT_CHOICES = [
        ('METAR','METAR'),
        ('TAF','TAF'),
    ]

    airport = models.ForeignKey(Airport, verbose_name=_("Airport"), on_delete=models.CASCADE, null=True)
    msg_encode = models.TextField(_("Message in Encoded Form"))
    msg_decode = models.JSONField(_("Decoded Message"), blank=True, null=True)
    msg_format = models.CharField(max_length=50, choices=MSG_FORMAT_CHOICES,
                                          verbose_name=_("Message Format"),)
    msg_datetime = models.DateTimeField(_("Message Datetime"), auto_now=False, auto_now_add=False, null=True)


class AviationPage(MetadataPageMixin, RoutablePageMixin, Page):
    template = "aviation/aviation_page.html"
    parent_page_types = ["home.HomePage"]
    subpage_types = []
    max_count = 1

    content_panels = Page.content_panels

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        latest_metar_message = Message.objects.filter(msg_format='METAR').order_by('-msg_datetime').first()
        latest_metar_datetime = latest_metar_message.msg_datetime.astimezone(timezone.utc).isoformat() if latest_metar_message else None

        abm_settings = AdminBoundarySettings.for_request(request)

        abm_extents = abm_settings.combined_countries_bounds

        stn_categories = AirportCategory.objects.all()

        context.update({
            'latest_metar_datetime': latest_metar_datetime,
            'bounds':abm_extents,
            'stn_categories':stn_categories
        })
        return context