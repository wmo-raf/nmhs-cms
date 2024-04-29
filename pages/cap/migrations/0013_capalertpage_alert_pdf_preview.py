# Generated by Django 4.2.3 on 2024-04-24 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0027_integrationsettings_google_site_verification_key'),
        ('cap', '0012_alter_capalertpage_info_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='capalertpage',
            name='alert_pdf_preview',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='base.customdocumentmodel'),
        ),
    ]
