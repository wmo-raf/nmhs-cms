# Generated by Django 4.1.5 on 2023-02-02 13:24

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, null=True, verbose_name='City Name')),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326, verbose_name='City Location')),
            ],
        ),
        migrations.CreateModel(
            name='Forecast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forecast_date', models.DateField()),
                ('max_temp', models.IntegerField(verbose_name='Maximum Temperature')),
                ('min_temp', models.IntegerField(verbose_name='Minimum Temperaure')),
                ('wind_direction', models.IntegerField()),
                ('wind_speed', models.IntegerField()),
                ('condition', models.CharField(max_length=255, null=True, verbose_name='Weather Condition')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.city')),
            ],
        ),
    ]
