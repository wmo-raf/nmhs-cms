# Generated by Django 4.1.9 on 2023-05-15 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0083_workflowcontenttype'),
        ('projects', '0001_initial'),
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectpage',
            name='youtube_playlist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='videos.youtubeplaylist', verbose_name='Youtube playlist'),
        ),
        migrations.AddField(
            model_name='projectindexpage',
            name='banner_image',
            field=models.ForeignKey(blank=True, help_text='A high quality image related to Projects', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Banner Image'),
        ),
        migrations.AddField(
            model_name='projectindexpage',
            name='call_to_action_related_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Call to action related page'),
        ),
        migrations.AddField(
            model_name='projectindexpage',
            name='introduction_button_link',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Introduction button link'),
        ),
        migrations.AddField(
            model_name='projectindexpage',
            name='introduction_image',
            field=models.ForeignKey(blank=True, help_text='A high quality image related to Projects', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Introduction Image'),
        ),
        migrations.AlterUniqueTogether(
            name='serviceproject',
            unique_together={('service', 'project')},
        ),
    ]