# Generated by Django 4.2.3 on 2024-02-28 09:31

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail_color_panel.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('cityclimate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataparameter',
            name='chart_config',
            field=wagtail.fields.StreamField([('line_chart', wagtail.blocks.StructBlock([('line_color', wagtail_color_panel.blocks.NativeColorBlock(default='#2caffe', label='Line Color'))], label='Line Chart')), ('bar_chart', wagtail.blocks.StructBlock([('orientation', wagtail.blocks.ChoiceBlock(choices=[('vertical', 'Vertical'), ('horizontal', 'Horizontal')])), ('fill_color', wagtail_color_panel.blocks.NativeColorBlock(default='#2caffe', label='Fill Color'))], label='Bar Chart')), ('area_chart', wagtail.blocks.StructBlock([('fill_color', wagtail_color_panel.blocks.NativeColorBlock(default='#2caffe', label='Area Fill Color'))], label='Area Chart'))], blank=True, null=True, use_json_field=True, verbose_name='Chart Configuration'),
        ),
    ]