# Generated by Django 4.2.7 on 2024-08-06 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0030_formfilesubmission'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menupermission',
            options={'default_permissions': [], 'permissions': (('can_view_geomanager_menu', 'Can view Geomanager menu'), ('can_view_survey_menu', 'Can View Survey menu'), ('can_view_alerts_menu', 'Can view CAP Alerts Menu'), ('can_view_forecast_menu', 'Can view Forecast Menu'), ('can_view_aviation_editor_menu', 'Can view Aviation Editor Menu'))},
        ),
    ]