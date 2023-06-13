# Generated by Django 4.1.9 on 2023-05-18 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webicons', '0001_initial'),
        ('core', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('order', models.PositiveIntegerField(default=0)),
                ('icon', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webicons.webicon')),
            ],
            options={
                'verbose_name': 'Product Group',
                'verbose_name_plural': 'Products Groups',
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('png', 'PNG'), ('pdf', 'PDF')], max_length=20)),
                ('classification', models.CharField(choices=[('forecast', 'Forecast'), ('monitoring', 'Monitoring')], default='forecast', max_length=100)),
                ('ordering', models.PositiveIntegerField(default=0)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_types', to='core.productgroup')),
            ],
            options={
                'verbose_name': 'Product Type',
                'verbose_name_plural': 'Products Types',
                'ordering': ['ordering'],
            },
        ),
    ]