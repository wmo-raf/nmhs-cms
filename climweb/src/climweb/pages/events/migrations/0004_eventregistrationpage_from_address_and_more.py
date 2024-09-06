# Generated by Django 4.2.2 on 2023-08-07 08:24

from django.db import migrations, models
import wagtail.contrib.forms.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_remove_eventregistrationpage_from_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventregistrationpage',
            name='from_address',
            field=models.EmailField(blank=True, max_length=255, verbose_name='from address'),
        ),
        migrations.AddField(
            model_name='eventregistrationpage',
            name='subject',
            field=models.CharField(blank=True, max_length=255, verbose_name='subject'),
        ),
        migrations.AddField(
            model_name='eventregistrationpage',
            name='to_address',
            field=models.CharField(blank=True, help_text='Optional - form submissions will be emailed to these addresses. Separate multiple addresses by comma.', max_length=255, validators=[wagtail.contrib.forms.models.validate_to_address], verbose_name='to address'),
        ),
    ]
