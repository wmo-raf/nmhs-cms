# Generated by Django 4.1.7 on 2023-04-02 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_alter_productpage_all_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productpage',
            name='all_products',
        ),
    ]