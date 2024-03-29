# Generated by Django 4.2.3 on 2024-01-11 09:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicationsindexpage',
            name='earliest_publication_year',
            field=models.PositiveIntegerField(default=2024, help_text='The year for the earliest available publication. This is used to generate the years available for filtering ', validators=[django.core.validators.MinValueValidator(2000), django.core.validators.MaxValueValidator(2024)], verbose_name='Earliest Publication Year'),
        ),
    ]
