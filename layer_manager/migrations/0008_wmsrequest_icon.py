# Generated by Django 4.1.7 on 2023-03-31 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webicons', '0004_alter_webicon_file'),
        ('layer_manager', '0007_wmsrequest_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='wmsrequest',
            name='icon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='webicons.webicon'),
        ),
    ]
