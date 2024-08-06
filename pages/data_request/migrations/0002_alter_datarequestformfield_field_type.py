# Generated by Django 4.2.7 on 2024-08-05 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_request', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datarequestformfield',
            name='field_type',
            field=models.CharField(choices=[('singleline', 'Single line text'), ('multiline', 'Multi-line text'), ('email', 'Email'), ('number', 'Number'), ('url', 'URL'), ('checkbox', 'Checkbox'), ('checkboxes', 'Checkboxes'), ('dropdown', 'Drop down'), ('multiselect', 'Multiple select'), ('radio', 'Radio buttons'), ('date', 'Date'), ('datetime', 'Date/time'), ('hidden', 'Hidden field'), ('image', 'Upload Image'), ('document', 'Upload PDF Document')], max_length=16, verbose_name='field type'),
        ),
    ]