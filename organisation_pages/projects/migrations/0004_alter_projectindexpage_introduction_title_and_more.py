# Generated by Django 4.1.9 on 2023-06-12 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_remove_projectpage_call_to_action_external_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectindexpage',
            name='introduction_title',
            field=models.CharField(help_text='Introduction section title', max_length=100, verbose_name='Introduction Title'),
        ),
        migrations.AlterField(
            model_name='projectpage',
            name='introduction_title',
            field=models.CharField(help_text='Introduction section title', max_length=100, verbose_name='Introduction Title'),
        ),
    ]
