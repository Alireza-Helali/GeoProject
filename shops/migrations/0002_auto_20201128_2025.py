# Generated by Django 3.1.3 on 2020-11-28 20:25
from django.db import migrations
import json
from django.contrib.gis.geos import fromstr
from pathlib import Path
from django.db import migrations

data_file_name = 'export.json'


def load_data(apps, schema_editor):
    shop = apps.get_model('shops', 'geoproject')
    jsonfile = Path(__file__).parents[2] / data_file_name
    with open(str(data_file_name)) as datafile:
        objects = json.load(datafile)
        for obj in objects:


class Migration(migrations.Migration):
    dependencies = [
        ('shops', '0001_initial'),
    ]

    operations = [
    ]
