# Generated by Django 4.1.9 on 2023-05-15 12:14

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
        ('taggit', '0004_alter_taggeditem_content_type_alter_taggeditem_tag'),
        ('core', '0001_initial'),
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        ('news', '0001_initial'),
        ('wagtailcore', '0083_workflowcontenttype'),
    ]

    operations = [
        migrations.AddField(
            model_name='newspage',
            name='projects',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='projects.projectpage', verbose_name='Relevant Projects'),
        ),
        migrations.AddField(
            model_name='newspage',
            name='services',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='core.servicecategory', verbose_name='Relevant Services'),
        ),
        migrations.AddField(
            model_name='newspage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', through='news.NewsPageTag', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='newsindexpage',
            name='banner_image',
            field=models.ForeignKey(blank=True, help_text='A high quality image related to News', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Banner Image'),
        ),
        migrations.AddField(
            model_name='newsindexpage',
            name='call_to_action_related_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Call to action related page'),
        ),
    ]
