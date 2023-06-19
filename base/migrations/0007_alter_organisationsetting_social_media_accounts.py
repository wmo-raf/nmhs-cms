# Generated by Django 4.2.2 on 2023-06-16 09:12

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtailiconchooser.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_remove_organisationsetting_facebook_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisationsetting',
            name='social_media_accounts',
            field=wagtail.fields.StreamField([('social_media_account', wagtail.blocks.StructBlock([('name', wagtail.blocks.CharBlock(max_length=60)), ('icon', wagtailiconchooser.blocks.IconChooserBlock(label='Icon', required=False)), ('full_url', wagtail.blocks.URLBlock(help_text='The full url link that takes you to the page', max_length=255))]))], blank=True, null=True, use_json_field=True),
        ),
    ]