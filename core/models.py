from django.template.defaultfilters import truncatechars
from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import MultiFieldPanel
from wagtail.documents.models import Document
from wagtail.documents.models import document_served
from wagtail.fields import RichTextField
from wagtail.models import Page
from wagtailmetadata.models import MetadataPageMixin

from nmhs_cms.settings.base import SUMMARY_RICHTEXT_FEATURES
from .utils import get_first_non_empty_p_string
from .wagtailsnippets_models import *


class CustomDocumentModel(Document):
    # Custom field
    download_count = models.IntegerField(default=0, blank=True, null=True)


def increment_document_download_count(instance, **kwargs):
    instance.download_count = instance.download_count + 1
    instance.save()


# Count documents download times
document_served.connect(increment_document_download_count)


class AbstractBannerPage(MetadataPageMixin, Page):
    class Meta:
        abstract = True

    banner_image = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name=_("Banner Image"),
        help_text=_("A high quality banner image"),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    banner_title = models.CharField(max_length=255, verbose_name=_('Banner Title'))
    banner_subtitle = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Banner Subtitle'))
    call_to_action_button_text = models.CharField(max_length=100, blank=True, null=True,
                                                  verbose_name=_('Call to action button text'))
    call_to_action_related_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name=_('Call to action related page')
    )

    content_panels = [
        MultiFieldPanel(
            [
                FieldPanel('banner_image'),
                FieldPanel('banner_title'),
                FieldPanel('banner_subtitle'),
                FieldPanel('call_to_action_button_text'),
                PageChooserPanel('call_to_action_related_page', )

            ],
            heading=_("Banner Section"),
        )
    ]

    def save(self, *args, **kwargs):
        if not self.search_image and self.banner_image:
            self.search_image = self.banner_image

        if not self.search_description and self.banner_title:
            # Limit the search meta desc to Google's 160 recommended chars
            self.search_description = truncatechars(self.banner_title, 160)
        return super().save(*args, **kwargs)


class AbstractBannerWithIntroPage(AbstractBannerPage):
    introduction_title = models.CharField(max_length=100, verbose_name=_('Call to action related page'),
                                          help_text=_("Introduction section title"), )
    introduction_text = RichTextField(features=SUMMARY_RICHTEXT_FEATURES, verbose_name=_('Introduction text'),
                                      help_text=_("Introduction section description"))
    introduction_image = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name=_("Introduction Image"),
        help_text=_("A high quality image"),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    introduction_button_text = models.TextField(max_length=20, blank=True, null=True,
                                                verbose_name=_("Introduction button text"), )
    introduction_button_link = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name=_("Introduction button link"),
    )

    class Meta:
        abstract = True

    content_panels = [
        *AbstractBannerPage.content_panels,
        MultiFieldPanel(
            [
                FieldPanel('introduction_title'),
                FieldPanel('introduction_image'),
                FieldPanel('introduction_text'),
                FieldPanel('introduction_button_text'),
                PageChooserPanel('introduction_button_link'),
            ],
            heading=_("Introduction Section"),
        ),
    ]

    def save(self, *args, **kwargs):
        if not self.search_description and self.introduction_text:
            p = get_first_non_empty_p_string(self.introduction_text)
            if p:
                # Limit the search meta desc to Google's 160 recommended chars
                self.search_description = truncatechars(p, 160)
        return super().save(*args, **kwargs)
