# Generated by Django 4.1.7 on 2023-05-02 11:22

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.documents.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0083_workflowcontenttype'),
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        ('about', '0008_alter_aboutpage_bottom_call_to_action_heading'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutpage',
            name='additional_materials',
            field=wagtail.fields.StreamField([('material', wagtail.blocks.StructBlock([('category', wagtail.blocks.CharBlock(max_length=255)), ('materials', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('type', wagtail.blocks.ChoiceBlock(choices=[('document', 'Document/File'), ('image', 'Image')])), ('title', wagtail.blocks.CharBlock(max_length=255)), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='Select document or file', required=False, verbose_name='Document/File')), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Select/upload image', required=False))])))]))], blank=True, null=True, use_json_field=True, verbose_name='Additional Materials'),
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='bottom_call_to_action_button_link',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Bottom call to action button link'),
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='bottom_call_to_action_button_text',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Bottom call to action button text'),
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='bottom_call_to_action_description',
            field=models.TextField(blank=True, null=True, verbose_name='Bottom call to action description'),
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='feature_block',
            field=wagtail.fields.StreamField([('feature_item', wagtail.blocks.StructBlock([('figure_type', wagtail.blocks.ChoiceBlock(choices=[('image', 'Image'), ('chart', 'Chart'), ('video', 'Video'), ('imageofchange', 'Image of Change')])), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('chart_config_url', wagtail.blocks.URLBlock(help_text='A URL that returns Highcharts.js configuration, including the data', required=False)), ('title', wagtail.blocks.CharBlock()), ('text', wagtail.blocks.TextBlock(label='Description')), ('action_link_text', wagtail.blocks.CharBlock(max_length=15, required=False)), ('action_link', wagtail.blocks.PageChooserBlock(label='Action Link Internal', required=False)), ('action_link_external', wagtail.blocks.URLBlock(help_text='An external link to a detailed resource on the internet.If provided, the internal link will be ignored', max_length=400, required=False))]))], blank=True, null=True, use_json_field=True, verbose_name='Feature Block'),
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='introduction_button_link',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Introduction Button Link'),
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='introduction_button_text',
            field=models.TextField(blank=True, max_length=20, null=True, verbose_name='Introduction Button Text'),
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='introduction_text',
            field=wagtail.fields.RichTextField(help_text='A short summary of your organisation as an organisation', verbose_name='Introduction Text'),
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='introduction_title',
            field=models.CharField(help_text='Introduction section title', max_length=100, verbose_name='Introduction Title'),
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='timeline_heading',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Timeline Heading'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='is_main',
            field=models.BooleanField(default=False, verbose_name='Is Main'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='logo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailimages.image', verbose_name='Logo'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='order',
            field=models.PositiveIntegerField(default=0, verbose_name='Order'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='visible_on_homepage',
            field=models.BooleanField(default=False, verbose_name='Visible on Homepage'),
        ),
        migrations.AlterField(
            model_name='partnerspage',
            name='banner_subtitle',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Banner Subtitle'),
        ),
        migrations.AlterField(
            model_name='partnerspage',
            name='banner_title',
            field=models.CharField(max_length=255, verbose_name='Banner Title'),
        ),
        migrations.AlterField(
            model_name='partnerspage',
            name='call_to_action_button_text',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Call to action button text'),
        ),
        migrations.AlterField(
            model_name='partnerspage',
            name='call_to_action_related_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Call to action related page'),
        ),
        migrations.AlterField(
            model_name='partnerspage',
            name='introduction_button_link',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Introduction button link'),
        ),
        migrations.AlterField(
            model_name='partnerspage',
            name='introduction_button_text',
            field=models.TextField(blank=True, max_length=20, null=True, verbose_name='Introduction button text'),
        ),
        migrations.AlterField(
            model_name='partnerspage',
            name='introduction_text',
            field=wagtail.fields.RichTextField(help_text='A summary of your organisation relations with partners', verbose_name='Introduction text'),
        ),
        migrations.AlterField(
            model_name='partnerspage',
            name='introduction_title',
            field=models.CharField(help_text='Introduction section title', max_length=100, verbose_name='Introduction title'),
        ),
    ]