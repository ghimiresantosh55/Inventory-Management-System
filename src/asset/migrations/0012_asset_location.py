# Generated by Django 3.2 on 2022-12-16 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse_location', '0001_initial'),
        ('asset', '0011_auto_20221127_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='asset_location', to='warehouse_location.location'),
            preserve_default=False,
        ),
    ]
