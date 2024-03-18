# Generated by Django 4.2.3 on 2024-03-13 11:53

from django.db import migrations, models
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_projectpage_goals_title_alter_projectpage_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectpage',
            name='goals_block',
            field=wagtail.fields.StreamField([('goal', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock()), ('description', wagtail.blocks.RichTextBlock(features=['bold', 'ul', 'ol', 'link', 'superscript', 'subscript', 'h2', 'h3', 'h4'])), ('image', wagtail.images.blocks.ImageChooserBlock(required=False))], label='Goal/Activity'))], blank=True, null=True, use_json_field=True, verbose_name='Goals/Activities List'),
        ),
        migrations.AlterField(
            model_name='projectpage',
            name='goals_title',
            field=models.CharField(blank=True, default='Our Areas of Work', max_length=200, null=True, verbose_name='Goals/Activities section title'),
        ),
    ]