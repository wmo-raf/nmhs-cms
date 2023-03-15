# Generated by Django 4.1.7 on 2023-03-15 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0083_workflowcontenttype'),
        ('core', '0009_remove_importantpages_all_foodsecuritystatements_page_and_more'),
        ('taggit', '0004_alter_taggeditem_content_type_alter_taggeditem_tag'),
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        ('products', '0005_alter_productdetailpage_month'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductDetailPage',
            new_name='ProductItemPage',
        ),
        migrations.RenameModel(
            old_name='ProductIndexPage',
            new_name='ProductPage',
        ),
        migrations.RenameModel(
            old_name='ProductsPage',
            new_name='ProductsIndexPage',
        ),
    ]
