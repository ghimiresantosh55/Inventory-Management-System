# Generated by Django 3.2 on 2022-11-09 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0009_asset_assetcategory_assetsubcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='assetlist',
            name='asset',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='asset_details', to='asset.asset'),
            preserve_default=False,
        ),
    ]
