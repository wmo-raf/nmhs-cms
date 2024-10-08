# Generated by Django 4.2.3 on 2023-08-29 09:58

import wagtail.blocks
import wagtail.fields
from django.db import migrations

from climweb.base.blocks import UUIDModelChooserBlock


class Migration(migrations.Migration):
    dependencies = [
        ('products', '0005_productpage_map_layers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productpage',
            name='map_layers',
            field=wagtail.fields.StreamField([('layers', wagtail.blocks.StructBlock([('geomanager_layer',
                                                                                      UUIDModelChooserBlock(
                                                                                          target_model='geomanager.rasterfilelayer')),
                                                                                     ('product_type',
                                                                                      wagtail.blocks.ChoiceBlock(
                                                                                          choices=[], required=False))],
                                                                                    label='Layer'))], blank=True,
                                             null=True, use_json_field=True, verbose_name='Map Layers'),
        ),
    ]
