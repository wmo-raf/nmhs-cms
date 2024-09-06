# Generated by Django 4.2.2 on 2023-06-14 19:24

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0001_initial'),
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        ('projects', '0001_initial'),
        ('wagtailcore', '0083_workflowcontenttype'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventpage',
            name='projects',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='projects.projectpage', verbose_name='Relevant Projects'),
        ),
        migrations.AddField(
            model_name='eventpage',
            name='search_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Search image'),
        ),
        migrations.AddField(
            model_name='eventindexpage',
            name='banner_image',
            field=models.ForeignKey(blank=True, help_text='A high quality banner image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Banner Image'),
        ),
        migrations.AddField(
            model_name='eventindexpage',
            name='call_to_action_related_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Call to action related page'),
        ),
        migrations.AddField(
            model_name='eventindexpage',
            name='search_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Search image'),
        ),
    ]
