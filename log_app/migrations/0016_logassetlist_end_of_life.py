# Generated by Django 3.1 on 2022-04-03 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_app', '0015_logassetlist_maintenance_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='logassetlist',
            name='end_of_life',
            field=models.DateField(blank=True, null=True),
        ),
    ]
