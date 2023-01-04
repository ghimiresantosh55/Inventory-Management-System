# Generated by Django 3.2 on 2022-06-03 05:12

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0019_alter_purchaseorderdetail_ref_purchase_order_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorderdetail',
            name='sale_cost',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=12),
        ),
    ]
