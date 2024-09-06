# Generated by Django 4.2 on 2023-07-17 20:04

import django.db.models.deletion
import wagtail.blocks
import wagtail.fields
import wagtailcache.cache
import wagtailmetadata.models
from django.db import migrations, models

from climweb.pages.satellite_imagery.utils import get_msg_layer_choices


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        ('wagtailcore', '0083_workflowcontenttype'),
    ]

    operations = [
        migrations.CreateModel(
            name='SatelliteImageryPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('msg_layers', wagtail.fields.StreamField([('msg_layer', wagtail.blocks.StructBlock([('name', wagtail.blocks.ChoiceBlock(choices=get_msg_layer_choices, label='Layer name')), ('label', wagtail.blocks.CharBlock(help_text='Leave blank to use default label title from EUMetView', label='Layer label', max_length=255, required=False))], label='MSG Layer'))], blank=True, null=True, use_json_field=True, verbose_name='MSG Layers')),
                ('search_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Search image')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtailmetadata.models.WagtailImageMetadataMixin, 'wagtailcore.page', models.Model, wagtailcache.cache.WagtailCacheMixin),
        ),
    ]
