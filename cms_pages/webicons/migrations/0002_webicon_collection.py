# Generated by Django 2.2.10 on 2020-04-25 16:40

from django.db import migrations, models
import django.db.models.deletion
import wagtail.models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('webicons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='webicon',
            name='collection',
            field=models.ForeignKey(default=wagtail.models.get_root_collection_id, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.Collection', verbose_name='collection'),
        ),
    ]
