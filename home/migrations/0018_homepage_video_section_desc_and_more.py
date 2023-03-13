# Generated by Django 4.1.7 on 2023-03-13 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_homepage_youtube_playlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='video_section_desc',
            field=models.CharField(default='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla accumsan, metus ultriceseleifend gt', max_length=250, null=True, verbose_name='Media Section Description'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='video_section_title',
            field=models.CharField(default='Latest Media', max_length=100, null=True, verbose_name='Media Section Title'),
        ),
    ]
