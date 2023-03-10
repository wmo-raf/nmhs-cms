# Generated by Django 4.1.7 on 2023-03-04 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        ('mediacenter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediaindexpage',
            name='banner_image',
            field=models.ForeignKey(blank=True, help_text='A high quality image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Banner Image'),
        ),
    ]
