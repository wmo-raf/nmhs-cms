# Generated by Django 4.1.5 on 2023-02-07 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forecast_manager', '0003_alter_city_location'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'City', 'verbose_name_plural': 'Cities'},
        ),
    ]
