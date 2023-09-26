# Generated by Django 4.2.3 on 2023-09-25 10:12

from django.db import migrations, models
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('glossary', '0006_glossaryitemdetailpage_local_definitions_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='glossarylanguage',
            name='language',
        ),
        migrations.AddField(
            model_name='glossarylanguage',
            name='name',
            field=models.CharField(default='Amharic', max_length=100, verbose_name='Language name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='glossaryitemdetailpage',
            name='local_definitions',
            field=wagtail.fields.StreamField([('definitions', wagtail.blocks.StructBlock([('language', wagtail.blocks.CharBlock(label='Language', required=True)), ('definition', wagtail.blocks.RichTextBlock(help_text='Definition of the term in the local language'))], label='Local Definition'))], blank=True, null=True, use_json_field=True, verbose_name='Local Definitions'),
        ),
    ]
