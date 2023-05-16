# Generated by Django 4.1.9 on 2023-05-15 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_initial'),
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='youtube_playlist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='videos.youtubeplaylist', verbose_name='Youtube Playlist'),
        ),
    ]