# Generated by Django 4.1.7 on 2023-02-28 15:08

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0004_alter_taggeditem_content_type_alter_taggeditem_tag'),
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        ('wagtailcore', '0083_workflowcontenttype'),
        ('core', '0005_remove_application_show_in_geoportal'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDetailPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('year', models.PositiveIntegerField(choices=[(2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023)], default=2023)),
                ('month', models.IntegerField(choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')], default=2)),
                ('summary', wagtail.fields.RichTextField(help_text='Summary of the product release')),
                ('document', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='core.customdocumentmodel')),
                ('image', models.ForeignKey(blank=True, help_text='Image that will appear as thumbnail', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'verbose_name': 'Product Bulletin',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ProductPageTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_tags', to='products.productdetailpage')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_items', to='taggit.tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('banner_title', models.CharField(max_length=255)),
                ('banner_subtitle', models.CharField(blank=True, max_length=255, null=True)),
                ('call_to_action_button_text', models.CharField(blank=True, max_length=100, null=True)),
                ('introduction_title', models.CharField(help_text='Introduction section title', max_length=100)),
                ('introduction_text', wagtail.fields.RichTextField(help_text='A description of what your organisation does under  this Product')),
                ('introduction_button_text', models.TextField(blank=True, max_length=20, null=True)),
                ('feature_block', wagtail.fields.StreamField([('feature_item', wagtail.blocks.StructBlock([('figure_type', wagtail.blocks.ChoiceBlock(choices=[('image', 'Image'), ('chart', 'Chart'), ('video', 'Video'), ('imageofchange', 'Image of Change')])), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('chart_config_url', wagtail.blocks.URLBlock(help_text='A URL that returns Highcharts.js configuration, including the data', required=False)), ('title', wagtail.blocks.CharBlock()), ('text', wagtail.blocks.TextBlock(label='Description')), ('action_link_text', wagtail.blocks.CharBlock(max_length=15, required=False)), ('action_link', wagtail.blocks.PageChooserBlock(label='Action Link Internal', required=False)), ('action_link_external', wagtail.blocks.URLBlock(help_text='An external link to a detailed resource on the internet.If provided, the internal link will be ignored', max_length=400, required=False))]))], blank=True, null=True, use_json_field=True)),
                ('earliest_bulletin_year', models.PositiveIntegerField(default=2023, help_text='The year for the earliest available bulletin. This is used to generate the years available for filtering ', validators=[django.core.validators.MinValueValidator(2000), django.core.validators.MaxValueValidator(2023)])),
                ('products_per_page', models.PositiveIntegerField(default=6, help_text='How many of this products should be visible on the landing page filter section ?', validators=[django.core.validators.MinValueValidator(6), django.core.validators.MaxValueValidator(20)])),
                ('banner_image', models.ForeignKey(blank=True, help_text='A high quality image related to this Product', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Banner Image')),
                ('call_to_action_related_page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page')),
                ('introduction_button_link', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page')),
                ('introduction_image', models.ForeignKey(blank=True, help_text='A high quality image related to this Product', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Introduction Image')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='core.productcategory')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.servicecategory')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AddField(
            model_name='productdetailpage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', through='products.ProductPageTag', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
