# Generated by Django 4.2.7 on 2024-08-05 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0029_alter_servicecategory_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormFileSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='form_files/%Y/%m/%d')),
                ('file_type', models.CharField(choices=[('image', 'Image'), ('document', 'Document')], default='image', max_length=255)),
            ],
            options={
                'verbose_name': 'File Submission',
                'verbose_name_plural': 'File Submissions',
            },
        ),
    ]
