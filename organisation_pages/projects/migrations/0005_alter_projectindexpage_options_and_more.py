# Generated by Django 4.1.7 on 2023-05-02 14:25

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.blocks
import wagtail.documents.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0083_workflowcontenttype'),
        ('about', '0010_alter_aboutindexpage_options_alter_aboutpage_options_and_more'),
        ('core', '0026_alter_eventtype_options_alter_application_order_and_more'),
        ('videos', '0002_alter_videogallerypage_introduction_and_more'),
        ('projects', '0004_projectpage_partners'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projectindexpage',
            options={'verbose_name': 'Project Index Page'},
        ),
        migrations.AlterField(
            model_name='projectindexpage',
            name='banner_subtitle',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Banner Subtitle'),
        ),
        migrations.AlterField(
            model_name='projectindexpage',
            name='banner_title',
            field=models.CharField(max_length=255, verbose_name='Banner Title'),
        ),
        migrations.AlterField(
            model_name='projectindexpage',
            name='call_to_action_button_text',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Call to action button text'),
        ),
        migrations.AlterField(
            model_name='projectindexpage',
            name='call_to_action_related_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Call to action related page'),
        ),
        migrations.AlterField(
            model_name='projectindexpage',
            name='introduction_button_link',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Introduction button link'),
        ),
        migrations.AlterField(
            model_name='projectindexpage',
            name='introduction_button_text',
            field=models.TextField(blank=True, max_length=20, null=True, verbose_name='Introduction button text'),
        ),
        migrations.AlterField(
            model_name='projectindexpage',
            name='introduction_text',
            field=wagtail.fields.RichTextField(help_text='A description of ORG Projects in general', verbose_name='Introduction text'),
        ),
        migrations.AlterField(
            model_name='projectindexpage',
            name='introduction_title',
            field=models.CharField(help_text='Introduction section title', max_length=100, verbose_name='Introduction title'),
        ),
        migrations.AlterField(
            model_name='projectindexpage',
            name='items_per_page',
            field=models.PositiveIntegerField(default=6, help_text='How many items should be visible on the projects landing page filter section ?', validators=[django.core.validators.MinValueValidator(6), django.core.validators.MaxValueValidator(20)], verbose_name='Items per page'),
        ),
        migrations.AlterField(
            model_name='projectpage',
            name='begin_date',
            field=models.DateField(verbose_name='Begin date'),
        ),
        migrations.AlterField(
            model_name='projectpage',
            name='call_to_action_button_text',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Call to action button text'),
        ),
        migrations.AlterField(
            model_name='projectpage',
            name='call_to_action_external_link',
            field=models.URLField(blank=True, help_text='External Link if applicable', null=True, verbose_name='Call to action external link'),
        ),
        migrations.AlterField(
            model_name='projectpage',
            name='call_to_action_related_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Call to action related page'),
        ),
        migrations.AlterField(
            model_name='projectpage',
            name='end_date',
            field=models.DateField(verbose_name='End date'),
        ),
        migrations.AlterField(
            model_name='projectpage',
            name='feature_block',
            field=wagtail.fields.StreamField([('feature_item', wagtail.blocks.StructBlock([('figure_type', wagtail.blocks.ChoiceBlock(choices=[('image', 'Image'), ('chart', 'Chart'), ('video', 'Video'), ('imageofchange', 'Image of Change')])), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('chart_config_url', wagtail.blocks.URLBlock(help_text='A URL that returns Highcharts.js configuration, including the data', required=False)), ('title', wagtail.blocks.CharBlock()), ('text', wagtail.blocks.TextBlock(label='Description')), ('action_link_text', wagtail.blocks.CharBlock(max_length=15, required=False)), ('action_link', wagtail.blocks.PageChooserBlock(label='Action Link Internal', required=False)), ('action_link_external', wagtail.blocks.URLBlock(help_text='An external link to a detailed resource on the internet.If provided, the internal link will be ignored', max_length=400, required=False))]))], blank=True, null=True, use_json_field=True, verbose_name='Feature block'),
        ),
        migrations.AlterField(
            model_name='projectpage',
            name='introduction_button_link',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Introduction button link'),
        ),
        migrations.AlterField(
            model_name='projectpage',
            name='introduction_button_link_external',
            field=models.URLField(blank=True, help_text='External Link if applicable. Ignored if internal page above is chosen', null=True, verbose_name='Introduction button link external'),
        ),
        migrations.AlterField(
            model_name='projectpage',
            name='introduction_button_text',
            field=models.TextField(blank=True, max_length=20, null=True, verbose_name='Introduction button text'),
        ),
        migrations.AlterField(
            model_name='projectpage',
            name='partners',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, related_name='projects', to='about.partner', verbose_name='Partners'),
        ),
        migrations.AlterField(
            model_name='projectpage',
            name='project_materials',
            field=wagtail.fields.StreamField([('material', wagtail.blocks.StructBlock([('category', wagtail.blocks.CharBlock(max_length=255)), ('materials', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('type', wagtail.blocks.ChoiceBlock(choices=[('document', 'Document/File'), ('image', 'Image')])), ('title', wagtail.blocks.CharBlock(max_length=255)), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='Select document or file', required=False, verbose_name='Document/File')), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Select/upload image', required=False))])))]))], blank=True, null=True, use_json_field=True, verbose_name='Project Materials'),
        ),
        migrations.AlterField(
            model_name='projectpage',
            name='services',
            field=modelcluster.fields.ParentalManyToManyField(related_name='projects', through='projects.ServiceProject', to='core.servicecategory', verbose_name='Services'),
        ),
        migrations.AlterField(
            model_name='projectpage',
            name='youtube_playlist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='videos.youtubeplaylist', verbose_name='Youtube playlist'),
        ),
    ]