# Generated by Django 4.2.3 on 2024-02-05 06:05

import datetime
from django.db import migrations, models
import wagtail.blocks
import wagtail.documents.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_alter_productitempage_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='productindexpage',
            name='group_menu_items_by_service',
            field=models.BooleanField(default=True, verbose_name='Group menu items by service'),
        ),
        migrations.AlterField(
            model_name='productitempage',
            name='products',
            field=wagtail.fields.StreamField([('image_product', wagtail.blocks.StructBlock([('product_type', wagtail.blocks.CharBlock(label='Product Type', required=True)), ('date', wagtail.blocks.DateBlock(default=datetime.date(2024, 2, 5), help_text='The date when this product becomes effective', label='Effective from', required=True)), ('valid_until', wagtail.blocks.DateBlock(help_text='The last day this product remains effective. Leave blank if not applicable', label='Effective until', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=True)), ('description', wagtail.blocks.RichTextBlock(label='Summary of the map/image information'))], label='Map/Image Product')), ('document_product', wagtail.blocks.StructBlock([('product_type', wagtail.blocks.CharBlock(label='Product Type', required=True)), ('thumbnail', wagtail.images.blocks.ImageChooserBlock(help_text='For example a screen grab of the cover page', label='Thumbnail of the document', required=False)), ('date', wagtail.blocks.DateBlock(default=datetime.date(2024, 2, 5), help_text='The date when this product becomes effective', label='Effective from', required=True)), ('valid_until', wagtail.blocks.DateBlock(help_text='The last day this product remains effective. Leave blank if not applicable', label='Effective until', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(label='Document', required=True)), ('description', wagtail.blocks.RichTextBlock(label='Summary of the document information'))], label='Document/Bulletin Product'))], use_json_field=True),
        ),
    ]