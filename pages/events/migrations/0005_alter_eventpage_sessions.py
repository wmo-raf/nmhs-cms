# Generated by Django 3.2.20 on 2023-09-01 10:32

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_eventregistrationpage_from_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpage',
            name='sessions',
            field=wagtail.fields.StreamField([('session', wagtail.blocks.StructBlock([('start_time', wagtail.blocks.DateTimeBlock(help_text='Session Start Time')), ('end_time', wagtail.blocks.DateTimeBlock(help_text='Session End Time')), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Session Image', required=False)), ('title', wagtail.blocks.TextBlock(help_text='Session title')), ('detail', wagtail.blocks.RichTextBlock(features=['bold', 'ul', 'ol', 'link', 'superscript', 'subscript', 'h2', 'h3', 'h4'], help_text='Detail', required=False)), ('roles', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('name', wagtail.blocks.CharBlock(help_text='Name of person', label='Name of person', max_length=255)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Select/upload image', required=False)), ('role', wagtail.blocks.ChoiceBlock(choices=[('moderator', 'Moderator'), ('speaker', 'Speaker'), ('rapporteur ', 'Rapporteur')], help_text='Select Role', required=False))])))]))], blank=True, null=True, use_json_field=True, verbose_name='Sessions'),
        ),
    ]
