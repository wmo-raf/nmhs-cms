# Generated by Django 4.2.7 on 2024-09-13 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cap', '0020_othercapsettings'),
    ]

    operations = [
        migrations.CreateModel(
            name='CAPAlertMQTTBroker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Provide a name to identify the broker', max_length=255, verbose_name='Name')),
                ('host', models.CharField(help_text='Provide the broker host name or IP address', max_length=255, verbose_name='Broker Host')),
                ('port', models.PositiveIntegerField(help_text='Provide the broker port number', verbose_name='Broker Port')),
                ('username', models.CharField(max_length=255, verbose_name='Broker Username')),
                ('new_password', models.CharField(blank=True, help_text='Enter a new password to update the stored password', max_length=255, verbose_name='Broker Password')),
                ('password', models.CharField(max_length=255)),
                ('is_wis2box', models.BooleanField(default=False, help_text='Check this box if you are providing the broker details of a wis2box.', verbose_name='Is WIS2Box Node')),
                ('topic', models.CharField(help_text='Provide the MQTT topic to publish the CAP alerts.', max_length=255, verbose_name='Topic')),
                ('wis2box_metadata_id', models.CharField(blank=True, help_text='Provide the metadata ID for your dataset registered in the wis2box. If you do not have this, please create a dataset in the wis2box before proceeding.', max_length=255, verbose_name='Dataset ID')),
                ('active', models.BooleanField(default=True, help_text='Automatically publish CAP alerts to this broker', verbose_name='Active')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('retry_on_failure', models.BooleanField(default=True, verbose_name='Retry on failure')),
            ],
            options={
                'verbose_name': 'MQTT Broker',
                'verbose_name_plural': 'MQTT Brokers',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='CAPAlertMQTTBrokerEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('FAILURE', 'Failure'), ('SUCCESS', 'Success')], default='PENDING', editable=False, max_length=40, verbose_name='Status')),
                ('retries', models.IntegerField(default=0, verbose_name='Retries')),
                ('error', models.TextField(blank=True, null=True, verbose_name='Last Error Message')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('alert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mqtt_broker_events', to='cap.capalertpage')),
                ('broker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='cap.capalertmqttbroker')),
            ],
            options={
                'verbose_name': 'MQTT Broker Event',
                'verbose_name_plural': 'MQTT Broker Events',
            },
        ),
    ]