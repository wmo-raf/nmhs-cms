from wagtail.admin.panels import FieldPanel
from wagtail.models import Page

from .mailchimp_page import BaseMailChimpPage
from django.db import models


class MailingListSubscriptionPage(BaseMailChimpPage, Page):
    template = 'mailing_list_subscription.html'
    parent_page_types = ['home.HomePage']
    subpage_types = []
    max_count = 1

    heading = models.CharField(max_length=255, blank=True, null=True, help_text="Heading")
    introduction_text = models.TextField(blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('heading'),
        FieldPanel('introduction_text'),
    ] + BaseMailChimpPage.content_panels

    def save(self, *args, **kwargs):
        if self.introduction_text:
            self.search_description = self.introduction_text

        super(MailingListSubscriptionPage, self).save(*args, **kwargs)


class MailChimpApiContact(models.Model):
    email = models.EmailField()
    source = models.TextField(blank=True)
    list_id = models.CharField(max_length=100, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.source:
            return "{} - via - {}".format(self.email, self.source)
        return self.email