# Generated by Django 4.1.7 on 2023-02-28 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0083_workflowcontenttype'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailChimpApiContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('source', models.TextField(blank=True)),
                ('list_id', models.CharField(blank=True, max_length=100)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MailingListSubscriptionPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('list_id', models.CharField(help_text='Enter the MailChimp list ID to use for this form', max_length=50, verbose_name='MailChimp List ID')),
                ('double_optin', models.BooleanField(default=True, help_text='Use double opt-in process for new subscribers', verbose_name='Double Opt-In')),
                ('thank_you_text', models.TextField(blank=True, help_text='Message to show on successful submission', null=True)),
                ('heading', models.CharField(blank=True, help_text='Heading', max_length=255, null=True)),
                ('introduction_text', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
    ]