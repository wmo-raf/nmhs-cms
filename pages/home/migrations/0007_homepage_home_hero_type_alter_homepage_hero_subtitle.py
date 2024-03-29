# Generated by Django 4.2.3 on 2023-08-13 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_homepage_weather_watch_header'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='home_hero_type',
            field=models.CharField(choices=[('wide', 'Wide Banner'), ('split', 'Split Banner')], default='split', max_length=50, verbose_name='Banner Type'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='hero_subtitle',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Subtitle'),
        ),
    ]
