# Generated by Django 4.0.10 on 2023-02-27 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_alter_contactpage_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactpage',
            name='location',
            field=models.CharField(help_text='Location of organisation', max_length=250, null=True),
        ),
    ]
