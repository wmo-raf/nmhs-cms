# Generated by Django 4.1.7 on 2023-05-02 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_alter_eventindexpage_banner_subtitle_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eventindexpage',
            options={'verbose_name': 'Event Index Page'},
        ),
        migrations.AlterModelOptions(
            name='eventpage',
            options={'ordering': ['-date_from'], 'verbose_name': 'Event Page'},
        ),
        migrations.AlterModelOptions(
            name='eventregistrationpage',
            options={'verbose_name': 'Event Registration Page'},
        ),
    ]
