# Generated by Django 3.1 on 2022-04-03 04:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0004_assetlist_warranty_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='assetlist',
            name='maintenance_duration',
            field=models.DurationField(default=datetime.timedelta(0)),
        ),
    ]
