# Generated by Django 4.1.7 on 2023-03-03 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forecast_manager', '0010_alter_conditioncategory_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conditioncategory',
            name='title',
            field=models.CharField(help_text='Weather Condition Title', max_length=50, unique=True, verbose_name='Weather Condtion Title'),
        ),
    ]
