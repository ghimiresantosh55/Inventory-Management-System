# Generated by Django 3.2 on 2022-11-01 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0003_auto_20221030_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='transferdetail',
            name='cancelled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='transfermaster',
            name='cancelled',
            field=models.BooleanField(default=False),
        ),
    ]