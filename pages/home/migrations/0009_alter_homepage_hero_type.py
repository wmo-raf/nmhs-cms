# Generated by Django 4.2.3 on 2023-08-13 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_rename_home_hero_type_homepage_hero_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='hero_type',
            field=models.CharField(choices=[('full', 'Full Banner'), ('half', 'Half Banner'), ('card', 'Card Banner')], default='card', max_length=50, verbose_name='Banner Type'),
        ),
    ]