# Generated by Django 4.2.3 on 2023-08-06 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventregistrationpage',
            name='from_address',
        ),
        migrations.RemoveField(
            model_name='eventregistrationpage',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='eventregistrationpage',
            name='to_address',
        ),
    ]
