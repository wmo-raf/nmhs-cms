import os
from datetime import datetime, timedelta
from itertools import groupby

from capeditor.models import Alert
from django.contrib.gis.db import models
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import MultiFieldPanel, FieldPanel
from wagtail.models import Page
from wagtail_color_panel.edit_handlers import NativeColorPanel
from wagtail_color_panel.fields import ColorField
from wagtailgeowidget.helpers import geosgeometry_str_to_struct
from wagtailmetadata.models import MetadataPageMixin

from forecast_manager.models import City, Forecast
from media_pages.news.models import NewsPage
from media_pages.publications.models import PublicationPage
from media_pages.videos.models import YoutubePlaylist
from organisation_pages.events.models import EventPage
from services.models import ServiceIndexPage


class HomePage(MetadataPageMixin, Page):
    template = "home_page.html"

    subpage_types = [
        'capeditor.AlertList',
        'contact.ContactPage',
        'services.ServicesPage',
        'products.ProductIndexPage',
        'feedback.FeedbackPage',
        'publications.PublicationsIndexPage',
        'videos.VideoGalleryPage',
        'news.NewsIndexPage',
        'mediacenter.MediaIndexPage',
        'about.AboutIndexPage',
        'events.EventIndexPage',
        'email_marketing.MailchimpMailingListSubscriptionPage',
        'surveys.SurveyPage',
        'email_marketing.MauticMailingListSubscriptionPage'
    ]
    parent_page_type = [
        'wagtailcore.Page'
    ]
    max_count = 1

    text_color = ColorField(blank=True, null=True, default="#f0f0f0", verbose_name=_("Text Color"))

    hero_title = models.CharField(blank=False, null=True, max_length=100, verbose_name=_('Title'),
                                  default='National Meteorological & Hydrological Services')
    hero_subtitle = models.CharField(blank=False, null=True, max_length=100, verbose_name=_('Subtitle Title'),
                                     default='Observing and understanding weather and climate')
    hero_banner = models.ForeignKey("wagtailimages.Image",
                                    on_delete=models.SET_NULL,
                                    null=True, blank=False, related_name="+", verbose_name=_("Hero Banner"))

    enable_weather_forecasts = models.BooleanField(blank=True, default=True,
                                                   verbose_name=_("Enable weather forecasts section"))
    enable_mapviewer_cta = models.BooleanField(blank=True, default=True, verbose_name=_("Enable mapviewer section"))
    mapviewer_cta_title = models.CharField(blank=True, null=True, max_length=100,
                                           verbose_name=_('Mapviewer Call to Action Title'),
                                           default='Explore Mapviewer')
    mapviewer_cta_url = models.URLField(verbose_name=_("Mapviewer URL"), blank=True, null=True)
    enable_media = models.BooleanField(blank=True, default=True, verbose_name=_("Enable media section"))
    youtube_playlist = models.ForeignKey(
        YoutubePlaylist,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name=_("Youtube Playlist")
    )

    video_section_title = models.CharField(blank=False, null=True, max_length=100,
                                           verbose_name=_('Media Section Title'), default='Latest Media')
    video_section_desc = models.TextField(blank=False, null=True, max_length=500,
                                          verbose_name=_('Media Section Description'),
                                          default='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla accumsan, metus ultriceseleifend gt')

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            NativeColorPanel('text_color'),
            FieldPanel('hero_title'),
            FieldPanel('hero_subtitle'),
            FieldPanel("hero_banner"),
        ], heading=_("Hero Section")),
        MultiFieldPanel([
            FieldPanel('enable_weather_forecasts'),
            # FieldPanel('hero_subtitle')
        ], heading=_("Weather forecasts Section")),
        MultiFieldPanel([
            FieldPanel('enable_mapviewer_cta'),
            FieldPanel('mapviewer_cta_title'),
            FieldPanel('mapviewer_cta_url')
        ], heading=_("Climate Section Section")),
        MultiFieldPanel([
            FieldPanel('enable_media'),
            FieldPanel('video_section_title'),
            FieldPanel('video_section_desc'),
            FieldPanel('youtube_playlist'),
        ], heading=_("Media Section"))

    ]

    class Meta:
        verbose_name = _("Home Page")
        verbose_name_plural = _("Home Pages")

    @cached_property
    def city_item(self):
        cities = City.objects.all()
        return {'cities': cities.values()}

    @cached_property
    def get_forecast_by_city(request):

        start_date_param = datetime.today()
        end_date_param = start_date_param + timedelta(days=6)
        forecast_data = Forecast.objects.filter(forecast_date__gte=start_date_param.date(),
                                                forecast_date__lte=end_date_param.date()) \
            .order_by('forecast_date') \
            .values('id', 'city__name', 'forecast_date', 'max_temp', 'min_temp', 'wind_speed', 'wind_direction',
                    'condition__title', 'condition__icon_image', 'condition__icon_image__file')
        # .annotate(
        #     forecast_date_str = Cast(
        #         TruncDate('forecast_date', DateField()), CharField(),
        #     ),
        # )

        # sort the data by city
        data_sorted = sorted(forecast_data, key=lambda x: x['city__name'])

        # group the data by city
        grouped_forecast = []
        for city, group in groupby(data_sorted, lambda x: x['city__name']):
            city_data = {'city': city, 'forecast_items': list(group)}

            for item in city_data['forecast_items']:
                # date_obj = datetime.strptime( item['forecast_date'], '%Y-%m-%d').date()
                item['forecast_date'] = item['forecast_date'].strftime('%a %d, %b').replace(' 0', ' ')

            grouped_forecast.append(city_data)

        return {
            'forecasts': grouped_forecast
        }

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
    def get_forecast_by_daterange(request):
        start_date_param = datetime.today()
        end_date_param = start_date_param + timedelta(days=6)
        forecast_data = Forecast.objects.filter(forecast_date__gte=start_date_param.date(),
                                                forecast_date__lte=end_date_param.date()) \
            .values('id', 'city__name', 'city__location', 'forecast_date', 'max_temp', 'min_temp', 'wind_speed',
                    'wind_direction', 'condition__title', 'condition__icon_image', 'condition__icon_image__file')

        # sort the data by date
        data_sorted = sorted(forecast_data, key=lambda x: x['forecast_date'])

        # group the data by date
        grouped_forecast = []
        for forecast_date, group in groupby(data_sorted, lambda x: x['forecast_date']):
            city_data = {
                'forecast_date': forecast_date.strftime('%a %d, %b').replace(' 0', ' '),
                'forecast_features': {}
            }

            forecast_features = []
            for forecast in list(group):
                location = geosgeometry_str_to_struct(str(forecast['city__location']))
                feature = {
                    "type": "Feature",
                    "properties": {
                        'id': forecast['id'],
                        'city_name': forecast['city__name'],
                        'forecast_date': forecast['forecast_date'].strftime('%a %d, %b').replace(' 0', ' '),
                        'max_temp': forecast['max_temp'],
                        'min_temp': forecast['min_temp'],
                        'wind_speed': forecast['wind_speed'],
                        'wind_direction': forecast['wind_direction'],
                        'media_path': f"{os.getenv('MEDIA_URL', '/media/')}",
                        'condition_icon': forecast['condition__icon_image__file'],
                        'condition_desc': forecast['condition__title'],
                    },
                    "geometry": {
                        "coordinates": [
                            location['x'],
                            location['y'],
                        ],
                        "type": "Point"
                    }
                }

                forecast_features.append(feature)

            city_data['forecast_features'] = {
                "type": "FeatureCollection",
                "features": forecast_features
            }

            grouped_forecast.append(city_data)

        return {
            'day_forecast': grouped_forecast
        }

    @cached_property
    def get_alerts(self):
        alerts = Alert.objects.all()
        active_alerts = alerts.filter(alert_info__expires__gte=datetime.today().date())[:3]
        return {
            # 'alerts': serializers.serialize('json',list(alerts) ),
            'alerts': alerts,
            'active_alerts': active_alerts
        }

    @cached_property
    def get_services(self):
        services = ServiceIndexPage.objects.live().public

        return {
            'services': services
        }

    @cached_property
    def get_cities(self):
        cities = City.objects.all()
        return {
            'cities': cities
        }
