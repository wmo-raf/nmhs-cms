# Generated by Django 4.1.9 on 2023-07-10 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        ('base', '0013_organisationsetting_country_flag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisationsetting',
            name='logo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Organisation Logo'),
        ),
    ]
