# Generated by Django 4.2 on 2023-07-17 10:39

from django.db import migrations, models
import django.db.models.deletion
import wagtail.contrib.routable_page.models
import wagtailcache.cache
import wagtailmetadata.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        ('wagtailcore', '0083_workflowcontenttype'),
    ]

    operations = [
        migrations.CreateModel(
            name='StationsPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('search_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Search image')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtailmetadata.models.WagtailImageMetadataMixin, wagtail.contrib.routable_page.models.RoutablePageMixin, 'wagtailcore.page', models.Model, wagtailcache.cache.WagtailCacheMixin),
        ),
    ]
