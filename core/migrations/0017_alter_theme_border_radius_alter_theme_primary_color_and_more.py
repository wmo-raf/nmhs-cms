# Generated by Django 4.1.7 on 2023-04-07 09:19

import django.core.validators
from django.db import migrations, models
import wagtail_color_panel.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_alter_theme_border_radius'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='border_radius',
            field=models.IntegerField(default=4, help_text='Minimum 0 and Maximum 100 in percentage', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Border radius (%)'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='primary_color',
            field=wagtail_color_panel.fields.ColorField(blank=True, default='#363636', help_text='Primary color (use color picker)', max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='theme',
            name='secondary_color',
            field=wagtail_color_panel.fields.ColorField(blank=True, default='#3488ce', help_text='Secondary color (use color picker)', max_length=7, null=True),
        ),
    ]
