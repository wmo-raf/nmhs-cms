# Generated by Django 4.2.3 on 2023-09-25 08:34

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.fields
import wagtailcache.cache
import wagtailmetadata.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0089_log_entry_data_json_null_to_object'),
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlossaryIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('introduction_title', models.CharField(help_text='Introduction section title', max_length=100, verbose_name='Introduction Title')),
                ('introduction_text', wagtail.fields.RichTextField(help_text='Introduction section description', verbose_name='Introduction text')),
                ('introduction_button_text', models.TextField(blank=True, max_length=20, null=True, verbose_name='Introduction button text')),
                ('introduction_button_link', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Introduction button link')),
                ('introduction_image', models.ForeignKey(blank=True, help_text='A high quality image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Introduction Image')),
                ('search_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Search image')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtailmetadata.models.WagtailImageMetadataMixin, 'wagtailcore.page', models.Model, wagtailcache.cache.WagtailCacheMixin),
        ),
        migrations.CreateModel(
            name='GlossaryLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('language', models.CharField(max_length=100)),
                ('parent', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='languages', to='glossary.glossaryindexpage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GlossaryItemDetailPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('term', models.CharField(help_text='The term to define', max_length=255, verbose_name='Term')),
                ('scientific_definition', wagtail.fields.RichTextField(help_text='Normal definition  of the term', verbose_name='Scientific definition')),
                ('simplified_definition', wagtail.fields.RichTextField(help_text='Simplified definition of the term ', verbose_name='Simplified definition')),
                ('search_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Search image')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtailmetadata.models.WagtailImageMetadataMixin, 'wagtailcore.page', models.Model, wagtailcache.cache.WagtailCacheMixin),
        ),
        migrations.CreateModel(
            name='GlossaryItemDefinition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('definition', wagtail.fields.RichTextField(help_text='Definition of the term in the selected language')),
                ('item', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='definitions', to='glossary.glossaryitemdetailpage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
