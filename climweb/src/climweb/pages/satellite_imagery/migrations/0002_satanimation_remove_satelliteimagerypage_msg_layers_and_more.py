# Generated by Django 4.2.2 on 2023-07-21 11:20

import django.db.models.deletion
import modelcluster.fields
import wagtail.blocks
import wagtail.fields
from django.db import migrations, models

from climweb.pages.satellite_imagery.models import get_upload_to
from climweb.pages.satellite_imagery.utils import get_msg_layer_choices


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0083_workflowcontenttype'),
        ('satellite_imagery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SatAnimation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField()),
                ('layer', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='satelliteimagerypage',
            name='msg_layers',
        ),
        migrations.CreateModel(
            name='SatelliteImagerySetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg_layers', wagtail.fields.StreamField([('msg_layer', wagtail.blocks.StructBlock([('name', wagtail.blocks.ChoiceBlock(choices=get_msg_layer_choices, label='Layer name')), ('label', wagtail.blocks.CharBlock(help_text='Leave blank to use default label title from EUMetView', label='Layer label', max_length=255, required=False)), ('enabled', wagtail.blocks.BooleanBlock(default=True, label='Enabled', required=False)), ('abstract', wagtail.blocks.TextBlock(help_text='Leave empty to set from EUMETVIEW Layer details', label='Layer Abstract', required=False))], label='MSG Layer'))], blank=True, null=True, use_json_field=True, verbose_name='MSG Layers')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SatAnimationImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('file', models.FileField(upload_to=get_upload_to)),
                ('sat_anim', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='satellite_imagery.satanimation')),
            ],
        ),
    ]