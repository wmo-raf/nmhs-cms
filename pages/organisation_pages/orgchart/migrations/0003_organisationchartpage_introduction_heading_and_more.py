# Generated by Django 4.2.7 on 2024-04-19 21:05

from django.db import migrations, models
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('orgchart', '0002_organisationchartpage_introduction_text_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisationchartpage',
            name='introduction_heading',
            field=models.CharField(blank=True, default='MEET OUR TEAM', help_text='Introduction section heading', max_length=100, null=True, verbose_name='Introduction Heading'),
        ),
        migrations.AlterField(
            model_name='organisationchartpage',
            name='introduction_text',
            field=wagtail.fields.RichTextField(blank=True, default="We're a team of scientists, meteroologist, analysists, software engineers and researchers.We are invigorated by challenging weather phenomena, thrive on surpassing previous records, and are dedicated to improving the world's conditions with each passing day. ", help_text='Introduction section description', null=True, verbose_name='Introduction text'),
        ),
        migrations.AlterField(
            model_name='organisationchartpage',
            name='introduction_title',
            field=models.CharField(blank=True, default='Weather and Climate through Us', help_text='Introduction section title', max_length=100, null=True, verbose_name='Introduction Title'),
        ),
    ]