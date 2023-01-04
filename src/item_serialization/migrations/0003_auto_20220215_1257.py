# Generated by Django 3.1 on 2022-02-15 07:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('warehouse_location', '0001_initial'),
        ('item_serialization', '0002_salepackingtypecode_sale_detail'),
        ('purchase', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='packingtypedetailcode',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='packingtypedetailcode',
            name='pack_type_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pack_type_detail_codes', to='item_serialization.packingtypecode', verbose_name='Packing Type Code'),
        ),
        migrations.AddField(
            model_name='packingtypecode',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='packingtypecode',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='location_pack_codes', to='warehouse_location.location', verbose_name='Pack Type Location'),
        ),
        migrations.AddField(
            model_name='packingtypecode',
            name='purchase_detail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pack_type_codes', to='purchase.purchasedetail', verbose_name='Purchase Detail'),
        ),
    ]
