# Generated by Django 4.1.7 on 2023-05-02 14:25

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.documents.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0083_workflowcontenttype'),
        ('tenders', '0002_rename_tendersindexpage_tenderspage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tenderdetailpage',
            options={'verbose_name': 'Tender Detail Page'},
        ),
        migrations.AlterModelOptions(
            name='tenderspage',
            options={'verbose_name': 'Tender Page'},
        ),
        migrations.AlterField(
            model_name='tenderdetailpage',
            name='additional_documents',
            field=wagtail.fields.StreamField([('additional_documents', wagtail.blocks.StructBlock([('type', wagtail.blocks.ChoiceBlock(choices=[('document', 'Document/File'), ('image', 'Image')])), ('title', wagtail.blocks.CharBlock(max_length=255)), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='Select document or file', required=False, verbose_name='Document/File')), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Select/upload image', required=False))]))], blank=True, null=True, use_json_field=True, verbose_name='Additional Documents'),
        ),
        migrations.AlterField(
            model_name='tenderdetailpage',
            name='description',
            field=wagtail.fields.RichTextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='tenderspage',
            name='banner_subtitle',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Banner Subtitle'),
        ),
        migrations.AlterField(
            model_name='tenderspage',
            name='banner_title',
            field=models.CharField(max_length=255, verbose_name='Banner Title'),
        ),
        migrations.AlterField(
            model_name='tenderspage',
            name='call_to_action_button_text',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Call to action button text'),
        ),
        migrations.AlterField(
            model_name='tenderspage',
            name='call_to_action_related_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Call to action related page'),
        ),
        migrations.AlterField(
            model_name='tenderspage',
            name='introduction_button_link',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Introduction button text'),
        ),
        migrations.AlterField(
            model_name='tenderspage',
            name='introduction_button_text',
            field=models.TextField(blank=True, max_length=20, null=True, verbose_name='Introduction button text'),
        ),
        migrations.AlterField(
            model_name='tenderspage',
            name='introduction_text',
            field=wagtail.fields.RichTextField(help_text='A description of tenders at your organisation', verbose_name='Introduction Text'),
        ),
        migrations.AlterField(
            model_name='tenderspage',
            name='introduction_title',
            field=models.CharField(help_text='Introduction section title', max_length=100, verbose_name='Introduction Title'),
        ),
        migrations.AlterField(
            model_name='tenderspage',
            name='items_per_page',
            field=models.PositiveIntegerField(default=6, help_text='How many items should be visible on the landing page filter section ?', validators=[django.core.validators.MinValueValidator(6), django.core.validators.MaxValueValidator(20)], verbose_name='Items per page'),
        ),
        migrations.AlterField(
            model_name='tenderspage',
            name='no_tenders_description_text',
            field=models.TextField(blank=True, help_text='Additional text to appear when there are no tenders,below the no tenders header text', null=True, verbose_name='No tenders description text'),
        ),
        migrations.AlterField(
            model_name='tenderspage',
            name='no_tenders_header_text',
            field=models.TextField(blank=True, help_text='Text to appear when there are no tenders', null=True, verbose_name='No tenders header text'),
        ),
    ]