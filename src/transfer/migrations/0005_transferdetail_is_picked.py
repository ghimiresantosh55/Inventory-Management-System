# Generated by Django 3.2 on 2022-11-01 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0004_auto_20221101_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='transferdetail',
            name='is_picked',
            field=models.BooleanField(default=False),
        ),
    ]
