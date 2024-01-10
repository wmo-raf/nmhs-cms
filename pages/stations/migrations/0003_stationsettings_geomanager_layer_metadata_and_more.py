# Generated by Django 4.2.3 on 2023-11-10 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geomanager', '0030_delete_stationsettings'),
        ('stations', '0002_stationsettings'),
    ]

    operations = [
        migrations.AddField(
            model_name='stationsettings',
            name='geomanager_layer_metadata',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='geomanager.metadata', verbose_name='Stations Layer Metadata'),
        ),
        migrations.AddField(
            model_name='stationsettings',
            name='geomanager_subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='geomanager.subcategory', verbose_name='Stations Layer SubCategory'),
        ),
        migrations.AddField(
            model_name='stationsettings',
            name='layer_title',
            field=models.CharField(blank=True, default='Stations', max_length=100, null=True, verbose_name='Stations Layer Title'),
        ),
        migrations.AddField(
            model_name='stationsettings',
            name='show_on_mapviewer',
            field=models.BooleanField(default=False, help_text='Check to show stations data on Mapviewer', verbose_name='Show on Mapviewer'),
        ),
    ]