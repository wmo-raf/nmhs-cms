# Generated by Django 4.2.3 on 2023-08-29 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_remove_importantpages_all_alerts_page'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productitemtype',
            options={},
        ),
        migrations.AddConstraint(
            model_name='productitemtype',
            constraint=models.UniqueConstraint(fields=('category', 'name'), name='unique_category_name'),
        ),
    ]