# Generated by Django 3.1 on 2022-04-01 09:50

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0002_auto_20220215_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='assetlist',
            name='amc_rate',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), help_text='Annual Maintenance Charge Rate', max_digits=4),
        ),
        migrations.AddField(
            model_name='assetlist',
            name='depreciation_method',
            field=models.IntegerField(choices=[(1, 'STRAIGHT-LINE'), (2, 'DECLINING-BALANCE')], default=1, help_text='deprecation method : 1 = STRAIGHT-LINE, 2 = DECLINING-BALANCE, default value is = 1'),
        ),
        migrations.AddField(
            model_name='assetlist',
            name='depreciation_rate',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), help_text='Rate of Depreciation', max_digits=4),
        ),
        migrations.AddField(
            model_name='assetlist',
            name='salvage_value',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), help_text='value of asset after its full use', max_digits=7),
        ),
    ]
