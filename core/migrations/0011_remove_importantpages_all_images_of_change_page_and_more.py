# Generated by Django 4.1.7 on 2023-03-27 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0083_workflowcontenttype'),
        ('core', '0010_importantpages_all_alerts_page'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='importantpages',
            name='all_images_of_change_page',
        ),
        migrations.AddField(
            model_name='importantpages',
            name='all_forecasts_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page'),
        ),
    ]