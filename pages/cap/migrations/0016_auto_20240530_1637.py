# Generated by Django 4.2.7 on 2024-05-30 13:37

from django.db import migrations
from wagtail.blocks import StreamValue

from pages.cap.models import CapAlertPage


def change_boundary_blocks_to_polygon(apps, schema_editor):
    alerts = CapAlertPage.objects.all()

    for cap_alert_page in alerts:
        alert_infos = cap_alert_page.info

        info_blocks = []
        should_save = False

        for info in alert_infos:
            rep = info.block.get_api_representation(info.value)
            areas = rep.get("area")

            for area in areas:
                print(f"Checking area type... '{area['type']}'")
                if area["type"] == "boundary_block":
                    area["type"] = "polygon_block"
                    area["value"]["polygon"] = area["value"]["boundary"]
                    should_save = True

            rep["area"] = areas

            stream_item = {
                "type": "alert_info",
                "value": rep
            }

            info_blocks.append(stream_item)

        if should_save:
            print(f"Converting '{cap_alert_page.title}' boundaries to polygon blocks")
            cap_alert_page.info = StreamValue(cap_alert_page.info.stream_block, info_blocks, is_lazy=True)
            cap_alert_page.save()


def backwards(apps, schema_editor):
    """nothing to do"""
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('cap', '0015_alter_capalertpage_info'),
    ]

    operations = [
        migrations.RenameField(
            model_name='capalertpage',
            old_name='identifier',
            new_name='guid'
        ),
        migrations.RunPython(change_boundary_blocks_to_polygon, backwards),
    ]
