# Generated by Django 4.2.2 on 2023-06-14 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newstype',
            name='is_alert',
        ),
        migrations.RemoveField(
            model_name='newstype',
            name='is_press_release',
        ),
        migrations.AddField(
            model_name='newstype',
            name='icon',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]