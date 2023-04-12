# Generated by Django 4.1.7 on 2023-04-07 09:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_theme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='border_radius',
            field=models.IntegerField(default=20, help_text='Minimum 0 and Maximum 100', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]