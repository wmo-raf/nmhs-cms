# Generated by Django 4.2.2 on 2023-08-07 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_importantpages_cap_feed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='importantpages',
            name='all_alerts_page',
        ),
    ]
