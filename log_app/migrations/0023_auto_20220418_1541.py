# Generated by Django 3.1 on 2022-04-18 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0009_auto_20220330_1425'),
        ('log_app', '0022_logchalanmaster_discount_rate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='logchalandetail',
            old_name='order_detail',
            new_name='ref_order_detail',
        ),
        migrations.RenameField(
            model_name='logchalanmaster',
            old_name='order_master',
            new_name='ref_order_master',
        ),
        migrations.AddField(
            model_name='logchalandetail',
            name='ref_purchase_detail',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='purchase.purchasedetail'),
        ),
        migrations.AlterField(
            model_name='logsaledetail',
            name='ref_purchase_detail',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='purchase.purchasedetail'),
        ),
    ]
