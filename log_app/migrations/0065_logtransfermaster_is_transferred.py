# Generated by Django 3.2 on 2022-11-01 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_app', '0064_logtransferdetail_is_picked'),
    ]

    operations = [
        migrations.AddField(
            model_name='logtransfermaster',
            name='is_transferred',
            field=models.BooleanField(default=False),
        ),
    ]
