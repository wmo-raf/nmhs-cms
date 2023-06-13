# Generated by Django 4.1.9 on 2023-06-09 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='climate_title',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='enable_climate',
        ),
        migrations.AddField(
            model_name='homepage',
            name='enable_mapviewer_cta',
            field=models.BooleanField(blank=True, default=True, verbose_name='Enable mapviewer section'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='mapviewer_cta_title',
            field=models.CharField(blank=True, default='Explore Mapviewer', max_length=100, null=True, verbose_name='Mapviewer Call to Action Title'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='mapviewer_cta_url',
            field=models.URLField(blank=True, null=True, verbose_name='Mapviewer URL'),
        ),
    ]