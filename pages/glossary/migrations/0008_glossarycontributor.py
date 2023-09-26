# Generated by Django 4.2.3 on 2023-09-25 10:25

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('glossary', '0007_remove_glossarylanguage_language_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlossaryContributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('name', models.CharField(help_text='Name of Contributor', max_length=100, verbose_name='Contributor name')),
                ('organisation', models.CharField(blank=True, help_text="Name of the contributor's organisation, if applicable", max_length=100, null=True, verbose_name='Organisation')),
                ('url', models.URLField(blank=True, help_text='Optional link to more details about the contributor or organisation', null=True, verbose_name='Optional link')),
                ('contact', models.TextField(blank=True, help_text='Optional contact details of the contributor or organisation ', null=True, verbose_name='Contact details')),
                ('parent', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='contributors', to='glossary.glossaryindexpage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
