# Generated by Django 3.1 on 2022-03-10 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0006_auto_20220310_1532'),
        ('log_app', '0005_auto_20220310_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='logorderdetail',
            name='purchase_detail',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='purchase.purchasedetail'),
        ),
    ]
