# Generated by Django 4.1.7 on 2023-04-10 08:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0006_remove_theme_bs_blur_rad_remove_theme_bs_color_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='box_shadow',
            field=models.IntegerField(default=3, help_text='Elevation value minimum 1 and maximum 24', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(24)], verbose_name='Box shadow'),
        ),
    ]