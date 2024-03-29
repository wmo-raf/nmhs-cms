# Generated by Django 4.2.2 on 2023-06-14 19:24

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields
import wagtailmetadata.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        ('wagtailcore', '0083_workflowcontenttype'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartnersPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('banner_title', models.CharField(max_length=255, verbose_name='Banner Title')),
                ('banner_subtitle', models.CharField(blank=True, max_length=255, null=True, verbose_name='Banner Subtitle')),
                ('call_to_action_button_text', models.CharField(blank=True, max_length=100, null=True, verbose_name='Call to action button text')),
                ('introduction_title', models.CharField(help_text='Introduction section title', max_length=100, verbose_name='Introduction Title')),
                ('introduction_text', wagtail.fields.RichTextField(help_text='Introduction section description', verbose_name='Introduction text')),
                ('introduction_button_text', models.TextField(blank=True, max_length=20, null=True, verbose_name='Introduction button text')),
                ('partners_cta_title', models.CharField(help_text='Partners call to action section title', max_length=100, verbose_name='Partners Call to Action title')),
                ('partners_cta_text', wagtail.fields.RichTextField(help_text='Call to action description text', verbose_name='Partners call to action text')),
                ('partners_cta_button_text', models.TextField(blank=True, max_length=20, null=True, verbose_name='Partners call to action button text')),
                ('banner_image', models.ForeignKey(blank=True, help_text='A high quality banner image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Banner Image')),
                ('call_to_action_related_page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Call to action related page')),
                ('introduction_button_link', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Introduction button link')),
                ('introduction_image', models.ForeignKey(blank=True, help_text='A high quality image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Introduction Image')),
                ('partners_cta_button_link', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Partners call to action page')),
                ('partners_cta_image', models.ForeignKey(blank=True, help_text='A high quality image related to the Partners call to action message', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Partners call to action Image')),
                ('search_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Search image')),
            ],
            options={
                'verbose_name': 'Partners Page',
            },
            bases=(wagtailmetadata.models.WagtailImageMetadataMixin, 'wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('link', models.URLField(blank=True, help_text='Link to the partners website', max_length=500, null=True, verbose_name="Link to partner's website")),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Order')),
                ('visible_on_homepage', models.BooleanField(default=False, verbose_name='Visible on Homepage')),
                ('is_main', models.BooleanField(default=False, verbose_name='Is Main')),
                ('logo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailimages.image', verbose_name='Logo')),
            ],
            options={
                'verbose_name': 'Partner',
                'ordering': ('order',),
            },
        ),
    ]
