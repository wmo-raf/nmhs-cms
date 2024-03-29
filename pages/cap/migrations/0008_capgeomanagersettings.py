# Generated by Django 4.2.3 on 2023-11-13 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0089_log_entry_data_json_null_to_object'),
        ('geomanager', '0030_delete_stationsettings'),
        ('cap', '0007_alter_capalertpage_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='CAPGeomanagerSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_on_mapviewer', models.BooleanField(default=False, help_text='Check to show cap alerts on MapViewer', verbose_name='Show on MapViewer')),
                ('layer_title', models.CharField(blank=True, default='Weather Alerts', max_length=100, null=True, verbose_name='CAP Alerts Layer Title')),
                ('auto_refresh_interval', models.IntegerField(blank=True, help_text='Refresh cap alerts on the map after this minutes. Leave blank to disable auto refreshing', null=True, verbose_name='Auto Refresh interval in minutes')),
                ('geomanager_layer_metadata', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='geomanager.metadata', verbose_name='CAP Layer Metadata')),
                ('geomanager_subcategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='geomanager.subcategory', verbose_name='Stations Layer SubCategory')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
