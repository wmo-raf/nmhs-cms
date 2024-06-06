# Generated by Django 4.2.7 on 2024-06-03 12:04

import capeditor.blocks
from django.db import migrations, models
import uuid
import wagtail.blocks
import wagtail.documents.blocks
import wagtail.fields
import wagtailmodelchooser.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('cap', '0016_auto_20240530_1637'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='capalertpage',
            options={'ordering': ['-sent'], 'verbose_name': 'CAP Alert'},
        ),
        migrations.AlterField(
            model_name='capalertpage',
            name='guid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique ID. Auto generated on creation.', unique=True, verbose_name='Id'),
        ),
        migrations.AlterField(
            model_name='capalertpage',
            name='info',
            field=wagtail.fields.StreamField([('alert_info', wagtail.blocks.StructBlock([('event', wagtail.blocks.ChoiceBlock(choices=capeditor.blocks.get_hazard_types, help_text='The text denoting the type of the subject event of the alert message. You can define hazards events monitored by your institution from CAP settings', label='Event')), ('category', wagtail.blocks.ChoiceBlock(choices=[('Geo', 'Geophysical'), ('Met', 'Meteorological'), ('Safety', 'General emergency and public safety'), ('Security', 'Law enforcement, military, homeland and local/private security'), ('Rescue', 'Rescue and recovery'), ('Fire', 'Fire suppression and rescue'), ('Health', 'Medical and public health'), ('Env', 'Pollution and other environmental'), ('Transport', 'Public and private transportation'), ('Infra', 'Utility, telecommunication, other non-transport infrastructure'), ('CBRNE', 'Chemical, Biological, Radiological, Nuclear or High-Yield Explosive threat or attack'), ('Other', 'Other events')], help_text='The code denoting the category of the subject event of the alert message', label='Category')), ('language', wagtail.blocks.ChoiceBlock(choices=[('en', 'English'), ('fr', 'French')], help_text='The code denoting the language of the alert message', label='Language', required=False)), ('urgency', wagtail.blocks.ChoiceBlock(choices=[('Immediate', 'Immediate - Responsive action SHOULD be taken immediately'), ('Expected', 'Expected - Responsive action SHOULD be taken soon (within next hour)'), ('Future', 'Future - Responsive action SHOULD be taken in the near future'), ('Past', 'Past - Responsive action is no longer required')], help_text='The code denoting the urgency of the subject event of the alert message', label='Urgency')), ('severity', wagtail.blocks.ChoiceBlock(choices=[('Extreme', 'Extreme - Extraordinary threat to life or property'), ('Severe', 'Severe - Significant threat to life or property'), ('Moderate', 'Moderate - Possible threat to life or property'), ('Minor', 'Minor - Minimal to no known threat to life or property')], help_text='The code denoting the severity of the subject event of the alert message', label='Severity')), ('certainty', wagtail.blocks.ChoiceBlock(choices=[('Observed', 'Observed - Determined to have occurred or to be ongoing'), ('Likely', 'Likely - Likely (percentage > ~50%)'), ('Possible', 'Possible - Possible but not likely (percentage <= ~50%)'), ('Unlikely', 'Unlikely - Not expected to occur (percentage ~ 0)')], help_text='The code denoting the certainty of the subject event of the alert message', label='Certainty')), ('headline', wagtail.blocks.CharBlock(help_text='The text headline of the alert message. Make it direct and actionable as possible while remaining short', label='Headline', max_length=160, required=False)), ('description', wagtail.blocks.TextBlock(help_text='The text describing the subject event of the alert message. An extended description of the hazard or event that occasioned this message', label='Description', required=True)), ('instruction', wagtail.blocks.TextBlock(help_text='The text describing the recommended action to be taken by recipients of the alert message', label='Instruction', required=False)), ('effective', wagtail.blocks.DateTimeBlock(help_text='The effective time of the information of the alert message. If not set, the sent date will be used', label='Effective', required=False)), ('onset', wagtail.blocks.DateTimeBlock(help_text='The expected time of the beginning of the subject event of the alert message', label='Onset', required=False)), ('expires', wagtail.blocks.DateTimeBlock(help_text='The expiry time of the information of the alert message. If not set, each recipient is free to set its own policy as to when the message is no longer in effect.', label='Expires', required=True)), ('responseType', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('response_type', wagtail.blocks.ChoiceBlock(choices=[('Shelter', 'Shelter - Take shelter in place or per instruction'), ('Evacuate', 'Evacuate - Relocate as instructed in the instruction'), ('Prepare', 'Prepare - Relocate as instructed in the instruction'), ('Execute', 'Execute - Execute a pre-planned activity identified in instruction'), ('Avoid', 'Avoid - Avoid the subject event as per the instruction'), ('Monitor', 'Monitor - Attend to information sources as described in instruction'), ('Assess', 'Assess - Evaluate the information in this message - DONT USE FOR PUBLIC ALERTS'), ('AllClear', 'All Clear - The subject event no longer poses a threat or concern and any follow on action is described in instruction'), ('None', 'No action recommended')], help_text='The code denoting the type of action recommended for the target audience', label='Response type'))], label='Response Type'), default=[], label='Response Types')), ('senderName', wagtail.blocks.CharBlock(help_text='The human-readable name of the agency or authority issuing this alert.', label='Sender name', max_length=255, required=False)), ('contact', wagtail.blocks.CharBlock(help_text='The text describing the contact for follow-up and confirmation of the alert message', label='Contact', max_length=255, required=False)), ('audience', wagtail.blocks.TextBlock(help_text='The text describing the intended audience of the alert message', label='Audience', required=False)), ('area', wagtail.blocks.StreamBlock([('polygon_block', wagtail.blocks.StructBlock([('areaDesc', wagtail.blocks.TextBlock(help_text='The text describing the affected area of the alert message', label='Affected areas / Regions')), ('polygon', capeditor.blocks.PolygonOrMultiPolygonFieldBlock(help_text='The paired values of points defining a polygon that delineates the affected area of the alert message', label='Polygon')), ('altitude', wagtail.blocks.CharBlock(help_text='The specific or minimum altitude of the affected area of the alert message', label='Altitude', max_length=100, required=False)), ('ceiling', wagtail.blocks.CharBlock(help_text='The maximum altitude of the affected area of the alert message.MUST NOT be used except in combination with the altitude element. ', label='Ceiling', max_length=100, required=False)), ('geocode', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('valueName', wagtail.blocks.TextBlock(help_text='User-assigned string designating the domain of the code. Acronyms SHOULD be represented in all capital letters without periods (e.g., SAME, FIPS, ZIP', label='Value Name')), ('value', wagtail.blocks.TextBlock(help_text='A string (which may represent a number) denoting the value itself', label='Value'))], label='Geocode', required=False), default=[]))], label='Draw Polygon')), ('circle_block', wagtail.blocks.StructBlock([('areaDesc', wagtail.blocks.TextBlock(help_text='The text describing the affected area of the alert message', label='Affected areas / Regions')), ('circle', capeditor.blocks.CircleFieldBlock(help_text='Drag the marker to change position', label='Circle')), ('altitude', wagtail.blocks.CharBlock(help_text='The specific or minimum altitude of the affected area of the alert message', label='Altitude', max_length=100, required=False)), ('ceiling', wagtail.blocks.CharBlock(help_text='The maximum altitude of the affected area of the alert message.MUST NOT be used except in combination with the altitude element. ', label='Ceiling', max_length=100, required=False)), ('geocode', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('valueName', wagtail.blocks.TextBlock(help_text='User-assigned string designating the domain of the code. Acronyms SHOULD be represented in all capital letters without periods (e.g., SAME, FIPS, ZIP', label='Value Name')), ('value', wagtail.blocks.TextBlock(help_text='A string (which may represent a number) denoting the value itself', label='Value'))], label='Geocode', required=False), default=[]))], label='Circle')), ('predefined_block', wagtail.blocks.StructBlock([('area', wagtailmodelchooser.blocks.ModelChooserBlock(label='Area', target_model='capeditor.predefinedalertarea')), ('altitude', wagtail.blocks.CharBlock(help_text='The specific or minimum altitude of the affected area of the alert message', label='Altitude', max_length=100, required=False)), ('ceiling', wagtail.blocks.CharBlock(help_text='The maximum altitude of the affected area of the alert message.MUST NOT be used except in combination with the altitude element. ', label='Ceiling', max_length=100, required=False)), ('geocode', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('valueName', wagtail.blocks.TextBlock(help_text='User-assigned string designating the domain of the code. Acronyms SHOULD be represented in all capital letters without periods (e.g., SAME, FIPS, ZIP', label='Value Name')), ('value', wagtail.blocks.TextBlock(help_text='A string (which may represent a number) denoting the value itself', label='Value'))], label='Geocode', required=False), default=[]))], label='Predefined Area'))], help_text='Polygon, Circle, or Predefined area', label='Alert Area')), ('resource', wagtail.blocks.StreamBlock([('file_resource', wagtail.blocks.StructBlock([('resourceDesc', wagtail.blocks.TextBlock(help_text='The text describing the type and content of the resource file', label='Resource Description')), ('file', wagtail.documents.blocks.DocumentChooserBlock())])), ('external_resource', wagtail.blocks.StructBlock([('resourceDesc', wagtail.blocks.TextBlock(help_text='The text describing the type and content of the resource file', label='Resource Description')), ('external_url', wagtail.blocks.URLBlock(help_text='Link to external resource. This can be for example a link to related websites. ', verbose_name='External Resource Link'))]))], help_text='Additional file with supplemental information related to this alert information', label='Resources', required=False)), ('parameter', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('valueName', wagtail.blocks.TextBlock(label='Name')), ('value', wagtail.blocks.TextBlock(label='Value'))], label='Parameter'), default=[], label='Parameters')), ('eventCode', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('valueName', wagtail.blocks.TextBlock(help_text='Name for the event code', label='Name')), ('value', wagtail.blocks.TextBlock(help_text='Value of the event code', label='Value'))], label='Event Code'), default=[], label='Event codes'))], label='Alert Information'))], use_json_field=True, verbose_name='Alert Information'),
        ),
        migrations.AlterField(
            model_name='capalertpage',
            name='msgType',
            field=models.CharField(choices=[('Alert', 'Alert - Initial information requiring attention by targeted recipients'), ('Update', 'Update - Updates and supersedes the earlier message(s) identified in referenced alerts'), ('Cancel', 'Cancel - Cancels the earlier message(s) identified in references')], default='Alert', help_text='The code denoting the nature of the alert message', max_length=100, verbose_name='Message Type'),
        ),
        migrations.AlterField(
            model_name='capalertpage',
            name='status',
            field=models.CharField(choices=[('Draft', 'Draft - A preliminary template or draft, not actionable in its current form'), ('Actual', 'Actual - Actionable by all targeted recipients'), ('Test', 'Test - Technical testing only, all recipients disregard'), ('Exercise', 'Exercise - Actionable only by designated exercise participants; exercise identifier SHOULD appear in note'), ('System', 'System - For messages that support alert network internal functions')], default='Actual', help_text='The code denoting the appropriate handling of the alert', max_length=50, verbose_name='Status'),
        ),
    ]
