# Generated by Django 4.1.9 on 2023-06-12 11:03

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        ('products', '0003_alter_productitempage_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='productitempage',
            name='search_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Search image'),
        ),
        migrations.AddField(
            model_name='productpage',
            name='search_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Search image'),
        ),
        migrations.AlterField(
            model_name='productpage',
            name='banner_image',
            field=models.ForeignKey(blank=True, help_text='A high quality banner image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Banner Image'),
        ),
        migrations.AlterField(
            model_name='productpage',
            name='introduction_image',
            field=models.ForeignKey(blank=True, help_text='A high quality image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Introduction Image'),
        ),
        migrations.AlterField(
            model_name='productpage',
            name='introduction_text',
            field=wagtail.fields.RichTextField(help_text='Introduction section description', verbose_name='Introduction text'),
        ),
    ]