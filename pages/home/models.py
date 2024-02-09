import json
from datetime import datetime, timedelta
from itertools import groupby

from adminboundarymanager.models import AdminBoundarySettings
from capeditor.constants import SEVERITY_MAPPING
from django.contrib.gis.db import models
from django.utils import timezone
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _
from forecastmanager.models import City, Forecast
from forecastmanager.site_settings import ForecastSetting
from wagtail.admin.panels import MultiFieldPanel, FieldPanel
from wagtail.api.v2.utils import get_full_url
from wagtail.fields import StreamField
from wagtail.models import Page, Site
from wagtail_color_panel.fields import ColorField

from base import blocks
from base.mixins import MetadataPageMixin
from pages.cap.models import CapAlertPage
from pages.events.models import EventPage
from pages.news.models import NewsPage
from pages.organisation_pages.partners.models import Partner
from pages.publications.models import PublicationPage
from pages.services.models import ServicePage
from pages.videos.models import YoutubePlaylist


class HomePage(MetadataPageMixin, Page):
    BANNER_TYPES = (
        ('full', 'Full Banner'),
        ('half', 'Half Banner'),
        ('card', 'Card Banner')
    )

    template = "home_page.html"

    subpage_types = [
        'contact.ContactPage',
        'services.ServiceIndexPage',
        'products.ProductIndexPage',
        'feedback.FeedbackPage',
        'publications.PublicationsIndexPage',
        'news.NewsIndexPage',
        'mediacenter.MediaIndexPage',
        'organisation.OrganisationIndexPage',
        'events.EventIndexPage',
        'surveys.SurveyPage',
        'email_subscription.MailchimpMailingListSubscriptionPage',
        'email_subscription.MauticMailingListSubscriptionPage',
        'data_request.DataRequestPage',
        'flex_page.FlexPage',
        'stations.StationsPage',
        'satellite_imagery.SatelliteImageryPage',
        'cityclimate.CityClimateDataPage',
        'cap.CapAlertListPage',
        'glossary.GlossaryIndexPage',
        'webstories.WebStoryListPage',
    ]
    parent_page_type = [
        'wagtailcore.Page'
    ]
    max_count = 1

    hero_title = models.CharField(max_length=100, verbose_name=_('Title'))
    hero_subtitle = models.CharField(blank=True, null=True, max_length=100, verbose_name=_('Subtitle'))
    hero_banner = models.ForeignKey("wagtailimages.Image", on_delete=models.SET_NULL, null=True, blank=False,
                                    related_name="+", verbose_name=_("Banner Image"))
    hero_text_color = ColorField(blank=True, null=True, default="#f0f0f0", verbose_name=_("Banner Text Color"))
    hero_type = models.CharField(_("Banner Type"), max_length=50, choices=BANNER_TYPES, default='full')

    show_city_forecast = models.BooleanField(default=True, verbose_name=_("Show city forecast section"))

    show_weather_watch = models.BooleanField(default=True, verbose_name=_("Show weather watch section"))
    weather_watch_header = models.CharField(max_length=100, default="Our Weather Watch",
                                            verbose_name=_("Weather Watch Section header"))
    show_mapviewer_cta = models.BooleanField(default=False, verbose_name=_("Show MapViewer button"))
    mapviewer_cta_title = models.CharField(max_length=100, blank=True, null=True, default='Explore on MapViewer',
                                           verbose_name=_('MapViewer Call to Action Title'))
    mapviewer_cta_url = models.URLField(blank=True, null=True, verbose_name=_("Mapviewer URL"), )

    youtube_playlist = models.ForeignKey(
        YoutubePlaylist,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name=_("Youtube Playlist")
    )

    feature_block = StreamField([
        ('feature_item', blocks.FeatureBlock()),
    ], null=True, blank=True, use_json_field=True, verbose_name=_("Feature block"))

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('hero_title'),
            FieldPanel('hero_subtitle'),
            FieldPanel("hero_banner"),
            # NativeColorPanel('hero_text_color'),
            FieldPanel('hero_type')
        ], heading=_("Banner Section")),
        MultiFieldPanel([
            FieldPanel('show_city_forecast'),
        ], heading=_("City Forecast Section")),
        MultiFieldPanel([
            FieldPanel('show_weather_watch'),
            FieldPanel('weather_watch_header'),
            FieldPanel('show_mapviewer_cta'),
            FieldPanel('mapviewer_cta_title'),
            FieldPanel('mapviewer_cta_url')
        ], heading=_("Weather Watch Section")),
        MultiFieldPanel([
            FieldPanel('youtube_playlist'),
        ], heading=_("Media Section")),
        MultiFieldPanel([
            FieldPanel('feature_block'),

        ], heading=_("Addditional Information")),

    ]

    class Meta:
        verbose_name = _("Home Page")
        verbose_name_plural = _("Home Pages")

    def get_context(self, request, *args, **kwargs):
        context = super(HomePage, self).get_context(
            request, *args, **kwargs)

        abm_settings = AdminBoundarySettings.for_request(request)
        abm_extents = abm_settings.combined_countries_bounds
        boundary_tiles_url = get_full_url(request, abm_settings.boundary_tiles_url)

        context.update({
            "bounds": abm_extents,
            "boundary_tiles_url": boundary_tiles_url
        })

        default_city = None
        city_ls = City.objects.all()

        site = Site.objects.get(is_default_site=True)
        forecast_setting = ForecastSetting.for_site(site)

        if len(city_ls) > 0:
            if forecast_setting.default_city:
                default_city = forecast_setting.default_city.id
            else:
                default_city = city_ls.order_by('name').first().id

        city = request.GET.get('city_id', default_city)

        if city:
            context['selected_city'] = City.objects.get(pk=city).name
            start_date_param = datetime.today()
            end_date_param = start_date_param + timedelta(days=6)
            forecast_data = Forecast.objects.filter(forecast_date__gte=start_date_param.date(),
                                                    forecast_date__lte=end_date_param.date(),
                                                    effective_period__whole_day=True, city__id=city) \
                .order_by('forecast_date') \
                .values('id', 'city__name', 'city__id', 'forecast_date', 'data_value',
                        'condition')

            # sort the data by city
            data_sorted = sorted(forecast_data, key=lambda x: x['city__id'])

            # group the data by city
            grouped_forecast = []
            for city, group in groupby(data_sorted, lambda x: x['city__id']):
                city_data = {'city': city, 'forecast_items': list(group)}

                for item in city_data['forecast_items']:
                    # date_obj = datetime.strptime( item['forecast_date'], '%Y-%m-%d').date()
                    item['forecast_date'] = item['forecast_date'].strftime('%a %d, %b').replace(' 0', ' ')
                    item['condition_display'] = dict(Forecast.CONDITION_CHOICES).get(item['condition'])
                grouped_forecast.append(city_data)

            context['grouped_forecast'] = grouped_forecast

        if self.youtube_playlist:
            context['youtube_playlist_url'] = self.youtube_playlist.get_playlist_items_api_url(request)

        return context

    @cached_property
    def partners(self):
        # get partners that should appear on the homepage
        partners = Partner.objects.filter(visible_on_homepage=True)[:7]
        return partners

    @cached_property
    def city_item(self):
        reordered_cities = None
        cities = City.objects.all().values('id', 'name')

        site = Site.objects.get(is_default_site=True)
        forecast_setting = ForecastSetting.for_site(site)

        default_city = forecast_setting.default_city

        if len(cities) > 0:
            if default_city:
                # Get all items except the target item
                other_cities = City.objects.exclude(id=default_city.id)

                # Combine the target item with the other items
                reordered_cities = [default_city] + list(other_cities)
            else:
                reordered_cities = sorted(cities, key=lambda x: x['name'])
        return {'cities': reordered_cities}

    @cached_property
    def latest_updates(self):
        updates = []

        # get latest news, publication, crop monitor, seasonal forecast, food security statement,
        news = NewsPage.objects.live().filter(is_visible_on_homepage=True).order_by('-date').first()
        events = EventPage.objects.live().filter(is_visible_on_homepage=True).order_by('-date_from').first()

        if events is None:
            events = EventPage.objects.live().order_by('-date_from').first()

        if news is None:
            news = NewsPage.objects.live().order_by('-date').first()

        publications = PublicationPage.objects.live().filter(is_visible_on_homepage=True).order_by(
            '-publication_date').first()

        if publications is None:
            publications = PublicationPage.objects.live().order_by('-publication_date').first()

        if news:
            updates.append(news)
        if events:
            updates.append(events)
        if publications:
            updates.append(publications)

        return updates

    @cached_property
    def get_forecast_by_daterange(self):
        start_date_param = datetime.today()
        end_date_param = start_date_param + timedelta(days=6)

        dates_ls = Forecast.objects.filter(forecast_date__gte=start_date_param.date(),
                                           forecast_date__lte=end_date_param.date(), condition__isnull=False) \
            .order_by('forecast_date') \
            .values_list('forecast_date', flat=True) \
            .distinct()

        return {
            'forecast_dates': dates_ls
        }

    @cached_property
    def cap_alerts(self):
        alerts = CapAlertPage.objects.all().live().order_by('-sent')
        active_alert_infos = []
        geojson = {"type": "FeatureCollection", "features": []}

        for alert in alerts:
            for info in alert.info:
                if info.value.get('expires').date() >= datetime.today().date():
                    start_time = info.value.get("effective") or alert.sent

                    if timezone.now() > start_time:
                        status = "Ongoing"
                    else:
                        status = "Expected"

                    area_desc = [area.get("areaDesc") for area in info.value.area]
                    area_desc = ",".join(area_desc)

                    alert_info = {
                        "status": status,
                        "url": alert.url,
                        "event": f"{info.value.get('event')} ({area_desc})",
                        "event_icon": info.value.event_icon,
                        "severity": SEVERITY_MAPPING[info.value.get("severity")]
                    }

                    active_alert_infos.append(alert_info)

                    if info.value.features:
                        for feature in info.value.features:
                            geojson["features"].append(feature)
        return {
            'active_alert_info': active_alert_infos,
            'geojson': json.dumps(geojson)
        }

    @cached_property
    def services(self):
        services = ServicePage.objects.live()
        return services
