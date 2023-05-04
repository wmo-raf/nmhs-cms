# Generated by Django 4.1.7 on 2023-05-02 14:25

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0083_workflowcontenttype'),
        ('core', '0026_alter_eventtype_options_alter_application_order_and_more'),
        ('news', '0003_newspage_projects'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsindexpage',
            options={'verbose_name': 'News Index Page'},
        ),
        migrations.AlterModelOptions(
            name='newspage',
            options={'verbose_name': 'News Page'},
        ),
        migrations.AlterField(
            model_name='newsindexpage',
            name='banner_subtitle',
            field=models.CharField(max_length=255, verbose_name='Banner Subtitle'),
        ),
        migrations.AlterField(
            model_name='newsindexpage',
            name='banner_title',
            field=models.CharField(max_length=255, verbose_name='Banner Title'),
        ),
        migrations.AlterField(
            model_name='newsindexpage',
            name='call_to_action_button_text',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Call to action button text'),
        ),
        migrations.AlterField(
            model_name='newsindexpage',
            name='call_to_action_related_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Call to action related page'),
        ),
        migrations.AlterField(
            model_name='newsindexpage',
            name='items_per_page',
            field=models.PositiveIntegerField(default=6, help_text='How many items should be visible on the news landing page filter section ?', validators=[django.core.validators.MinValueValidator(6), django.core.validators.MaxValueValidator(20)], verbose_name='Items per page'),
        ),
        migrations.AlterField(
            model_name='newspage',
            name='body',
            field=wagtail.fields.RichTextField(verbose_name='Body'),
        ),
        migrations.AlterField(
            model_name='newspage',
            name='external_links',
            field=wagtail.fields.StreamField([('link', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=255)), ('link', wagtail.blocks.URLBlock(max_length=255))]))], blank=True, null=True, use_json_field=True, verbose_name='Extra links'),
        ),
        migrations.AlterField(
            model_name='newspage',
            name='extra_links_heading',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Extra links heading'),
        ),
        migrations.AlterField(
            model_name='newspage',
            name='feature_img_src',
            field=models.TextField(blank=True, null=True, verbose_name='Feature Image'),
        ),
        migrations.AlterField(
            model_name='newspage',
            name='is_alert',
            field=models.BooleanField(default=False, help_text='Is this an alert ?', verbose_name='Is alert'),
        ),
        migrations.AlterField(
            model_name='newspage',
            name='is_featured',
            field=models.BooleanField(default=False, help_text='Should this news appear on the news landing paging as the featured one ?', verbose_name='Is featured'),
        ),
        migrations.AlterField(
            model_name='newspage',
            name='is_visible_on_homepage',
            field=models.BooleanField(default=False, help_text='Should this appear in the homepage as an alert/latest update ?', verbose_name='Is visible on homepage'),
        ),
        migrations.AlterField(
            model_name='newspage',
            name='news_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.newstype', verbose_name='News type'),
        ),
        migrations.AlterField(
            model_name='newspage',
            name='subtitle',
            field=models.TextField(blank=True, help_text='Optional subtitle', null=True, verbose_name='Subtitle'),
        ),
    ]