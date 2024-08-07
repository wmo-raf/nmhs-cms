# Generated by Django 4.2.7 on 2024-07-01 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        ('products', '0024_alter_productitempage_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='productpage',
            name='default_listing_thumbnail',
            field=models.ForeignKey(blank=True, help_text='An image that will be used as a thumbnail for in the products listing, if no image can be extracted from product items', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Default Listing Thumbnail'),
        ),
    ]
