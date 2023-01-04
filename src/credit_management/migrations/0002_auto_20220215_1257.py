# Generated by Django 3.1 on 2022-02-15 07:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('credit_management', '0001_initial'),
        ('core_app', '0002_auto_20220215_1257'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sale', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditpaymentdetail',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='creditpaymentdetail',
            name='credit_clearance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='credit_payment_details', to='credit_management.creditclearance'),
        ),
        migrations.AddField(
            model_name='creditpaymentdetail',
            name='payment_mode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core_app.paymentmode'),
        ),
        migrations.AddField(
            model_name='creditclearance',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='creditclearance',
            name='ref_credit_clearance',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='credit_management.creditclearance'),
        ),
        migrations.AddField(
            model_name='creditclearance',
            name='sale_master',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sale.salemaster'),
        ),
    ]