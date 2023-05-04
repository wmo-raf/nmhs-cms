# Generated by Django 4.1.7 on 2023-05-02 12:56

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_delete_theme'),
        ('videos', '0001_initial'),
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        ('wagtailcore', '0083_workflowcontenttype'),
        ('services', '0014_servicespage_alter_serviceindexpage_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('banner_title', models.CharField(max_length=255, null=True, verbose_name='Banner Title')),
                ('banner_subtitle', models.CharField(max_length=255, null=True, verbose_name='Banner Subtitle')),
                ('call_to_action_button_text', models.CharField(blank=True, max_length=100, null=True, verbose_name='Call to action button text')),
                ('call_to_action_external_link', models.URLField(blank=True, help_text='External Link if applicable', null=True, verbose_name='Call to action external link')),
                ('introduction_title', models.CharField(help_text='Introduction section title', max_length=100, null=True, verbose_name='Introduction title')),
                ('introduction_text', wagtail.fields.RichTextField(help_text='A description of what ORG does under  this Service', null=True)),
                ('introduction_button_text', models.TextField(blank=True, max_length=20, null=True, verbose_name='Introduction button text')),
                ('introduction_button_link_external', models.URLField(blank=True, help_text='External Link if applicable. Ignored if internal page above is chosen', null=True, verbose_name='Introduction button link external')),
                ('what_we_do_button_text', models.TextField(blank=True, max_length=20, null=True, verbose_name='What we do button text')),
                ('projects_description', wagtail.fields.RichTextField(blank=True, help_text='Projects description text', null=True, verbose_name='Project Description')),
                ('feature_block_items', wagtail.fields.StreamField([('feature_item', wagtail.blocks.StructBlock([('figure_type', wagtail.blocks.ChoiceBlock(choices=[('image', 'Image'), ('chart', 'Chart'), ('video', 'Video'), ('imageofchange', 'Image of Change')])), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('chart_config_url', wagtail.blocks.URLBlock(help_text='A URL that returns Highcharts.js configuration, including the data', required=False)), ('title', wagtail.blocks.CharBlock()), ('text', wagtail.blocks.TextBlock(label='Description')), ('action_link_text', wagtail.blocks.CharBlock(max_length=15, required=False)), ('action_link', wagtail.blocks.PageChooserBlock(label='Action Link Internal', required=False)), ('action_link_external', wagtail.blocks.URLBlock(help_text='An external link to a detailed resource on the internet.If provided, the internal link will be ignored', max_length=400, required=False))]))], blank=True, null=True, use_json_field=True, verbose_name='Feature block items')),
                ('banner_image', models.ForeignKey(blank=True, help_text='A high quality image related to this Service', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Banner Image')),
                ('call_to_action_related_page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Call to action related page')),
                ('introduction_button_link', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Introduction button link')),
                ('introduction_image', models.ForeignKey(blank=True, help_text='A high quality image related to this Service', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Introduction Image')),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.servicecategory')),
                ('what_we_do_button_link', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='What we do button link')),
                ('youtube_playlist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='videos.youtubeplaylist', verbose_name='Youtube playlist')),
            ],
            options={
                'verbose_name': 'Service Page',
                'verbose_name_plural': 'Service Pages',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.RemoveField(
            model_name='serviceindexpage',
            name='banner_image',
        ),
        migrations.RemoveField(
            model_name='serviceindexpage',
            name='banner_subtitle',
        ),
        migrations.RemoveField(
            model_name='serviceindexpage',
            name='banner_title',
        ),
        migrations.RemoveField(
            model_name='serviceindexpage',
            name='call_to_action_button_text',
        ),
        migrations.RemoveField(
            model_name='serviceindexpage',
            name='call_to_action_external_link',
        ),
        migrations.RemoveField(
            model_name='serviceindexpage',
            name='call_to_action_related_page',
        ),
        migrations.RemoveField(
            model_name='serviceindexpage',
            name='feature_block_items',
        ),
        migrations.RemoveField(
            model_name='serviceindexpage',
            name='introduction_button_link',
        ),
        migrations.RemoveField(
            model_name='serviceindexpage',
            name='introduction_button_link_external',
        ),
        migrations.RemoveField(
            model_name='serviceindexpage',
            name='introduction_button_text',
        ),
        migrations.RemoveField(
            model_name='serviceindexpage',
            name='introduction_image',
        ),
        migrations.RemoveField(
            model_name='serviceindexpage',
            name='introduction_text',
        ),
        migrations.RemoveField(
            model_name='serviceindexpage',
            name='introduction_title',
        ),
        migrations.RemoveField(
            model_name='serviceindexpage',
            name='projects_description',
        ),
        migrations.RemoveField(
            model_name='serviceindexpage',
            name='service',
        ),
        migrations.RemoveField(
            model_name='serviceindexpage',
            name='what_we_do_button_link',
        ),
        migrations.RemoveField(
            model_name='serviceindexpage',
            name='what_we_do_button_text',
        ),
        migrations.RemoveField(
            model_name='serviceindexpage',
            name='youtube_playlist',
        ),
        migrations.DeleteModel(
            name='ServicesPage',
        ),
    ]