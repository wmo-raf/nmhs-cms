# Generated by Django 4.1.7 on 2023-02-28 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0083_workflowcontenttype'),
        ('core', '0004_application_serviceapplication_application_services_and_more'),
        ('videos', '0001_initial'),
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        ('services', '0003_alter_servicepage_banner_image_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ServicePage',
            new_name='ServicesPage',
        ),
    ]
