# Generated by Django 3.1 on 2022-03-30 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_auto_20220215_1257'),
        ('purchase', '0007_auto_20220327_1502'),
        ('log_app', '0010_auto_20220327_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logpurchasedetail',
            name='item_category',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='item.itemcategory'),
        ),
        migrations.AlterField(
            model_name='logpurchasedetail',
            name='purchase',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='purchase.purchasemaster'),
        ),
    ]
