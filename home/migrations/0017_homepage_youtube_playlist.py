# Generated by Django 4.1.7 on 2023-03-13 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
        ('home', '0016_delete_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='youtube_playlist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='videos.youtubeplaylist'),
        ),
    ]
