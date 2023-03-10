# Generated by Django 4.1.7 on 2023-03-03 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forecast_manager', '0004_alter_city_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forecast',
            name='wind_direction',
            field=models.IntegerField(blank=True, null=True, verbose_name='Wind Direction'),
        ),
        migrations.AlterField(
            model_name='forecast',
            name='wind_speed',
            field=models.IntegerField(blank=True, null=True, verbose_name='Wind Speed'),
        ),
    ]
