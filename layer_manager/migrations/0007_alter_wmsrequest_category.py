# Generated by Django 4.1.7 on 2023-03-24 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('layer_manager', '0006_layercategory_wmsrequest_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wmsrequest',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='layer_manager.layercategory', verbose_name='Layer categories'),
        ),
    ]
