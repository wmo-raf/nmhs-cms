# Generated by Django 4.2.7 on 2024-07-19 19:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("aviation", "0003_alter_station_options_alter_station_location_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="message",
            name="msg_datetime",
            field=models.DateTimeField(null=True, verbose_name="Message Datetime"),
        ),
        migrations.AlterField(
            model_name="message",
            name="msg_format",
            field=models.CharField(
                choices=[("METAR", "METAR"), ("TAF", "TAF")],
                max_length=50,
                verbose_name="Message Format",
            ),
        ),
        migrations.AlterField(
            model_name="station",
            name="id",
            field=models.CharField(primary_key=True, serialize=False, unique=True),
        ),
    ]
