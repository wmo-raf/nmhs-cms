# Generated by Django 4.1.9 on 2023-06-12 17:06

from django.db import migrations, models
import wagtail.blocks
import wagtail.documents.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_remove_productitempage_document_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productitempage',
            name='products',
            field=wagtail.fields.StreamField([('image_product', wagtail.blocks.StructBlock([('product_type', wagtail.blocks.CharBlock(required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('description', wagtail.blocks.RichTextBlock())], label='Image')), ('document_product', wagtail.blocks.StructBlock([('product_type', wagtail.blocks.CharBlock(required=True)), ('thumbnail', wagtail.images.blocks.ImageChooserBlock(required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=True)), ('description', wagtail.blocks.RichTextBlock())], label='Document'))], blank=True, null=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='productpage',
            name='introduction_title',
            field=models.CharField(help_text='Introduction section title', max_length=100, verbose_name='Introduction Title'),
        ),
    ]
