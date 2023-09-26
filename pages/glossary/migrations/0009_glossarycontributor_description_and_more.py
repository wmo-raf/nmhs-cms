# Generated by Django 4.2.3 on 2023-09-25 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glossary', '0008_glossarycontributor'),
    ]

    operations = [
        migrations.AddField(
            model_name='glossarycontributor',
            name='description',
            field=models.TextField(blank=True, help_text='Optional details about the contributor or their organisation', null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='glossarycontributor',
            name='organisation',
            field=models.CharField(blank=True, help_text="Optional name of the contributor's organisation, if applicable", max_length=100, null=True, verbose_name='Organisation'),
        ),
        migrations.AlterField(
            model_name='glossarycontributor',
            name='url',
            field=models.URLField(blank=True, help_text='Optional link to more details about the contributor or organisation', null=True, verbose_name='Link'),
        ),
    ]
