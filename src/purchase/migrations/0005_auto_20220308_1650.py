# Generated by Django 3.1 on 2022-03-08 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0004_delete_warehouselocation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasedetail',
            name='ref_purchase_detail',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='self_ref_purchase_detail', to='purchase.purchasedetail'),
        ),
    ]