# Generated by Django 4.1.7 on 2023-05-02 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0083_workflowcontenttype'),
        ('services', '0011_alter_serviceindexpage_options_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ServicesPage',
            new_name='ServicePage',
        ),
    ]