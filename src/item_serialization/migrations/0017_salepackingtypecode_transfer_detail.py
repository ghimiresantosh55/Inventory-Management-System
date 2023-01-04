# Generated by Django 3.2 on 2022-09-15 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0002_alter_transfermaster_branch'),
        ('item_serialization', '0016_salepackingtypecode_chalan_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='salepackingtypecode',
            name='transfer_detail',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='transfer_packing_types', to='transfer.transferdetail', verbose_name='Transfer Detail'),
        ),
    ]
