# Generated by Django 3.2 on 2022-09-12 08:26

from decimal import Decimal
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('item', '0005_alter_item_basic_info'),
        ('core_app', '0013_alter_currency_name'),
        ('purchase', '0023_alter_purchasedetail_batch_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransferMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date_ad', models.DateTimeField()),
                ('created_date_bs', models.CharField(max_length=10)),
                ('device_type', models.PositiveBigIntegerField(choices=[(1, 'Mobile'), (2, 'PC'), (3, 'Tablet'), (4, 'Other'), (5, 'NA')], default=5, help_text='where 1=Mobile, 2=PC, 3=Tablet and 4=Other')),
                ('app_type', models.PositiveBigIntegerField(choices=[(1, 'Web-App'), (2, 'IOS-App'), (3, 'Android-App'), (4, 'NA')], default=4, help_text='where 1=Web-App, 2=IOS-APP, 3=Android-APP')),
                ('transfer_type', models.CharField(choices=[(1, 'TRANSFER'), (2, 'RETURN')], max_length=20)),
                ('transfer_no', models.CharField(help_text='Transfer No should be of max 20 characters', max_length=20, unique=True)),
                ('sub_total', models.DecimalField(decimal_places=2, default=0.0, help_text='Sub total can have max value upto=9999999999.99 and default=0.0', max_digits=12)),
                ('discount_rate', models.DecimalField(decimal_places=2, default=0.0, help_text='Discount rate if applicable, default=0.0 and max_value upto=100.00', max_digits=5)),
                ('total_discountable_amount', models.DecimalField(decimal_places=2, default=0.0, help_text='Total discountable amount can have max value upto=9999999999.99 and default=0.0', max_digits=12)),
                ('total_taxable_amount', models.DecimalField(decimal_places=2, default=0.0, help_text='Total taxable amount can have max value upto=9999999999.99 and default=0.0', max_digits=12)),
                ('total_non_taxable_amount', models.DecimalField(decimal_places=2, default=0.0, help_text='Total nontaxable amount can have max value upto=9999999999.99 and default=0.0', max_digits=12)),
                ('total_discount', models.DecimalField(decimal_places=2, default=0.0, help_text='Total discount can have max value upto=9999999999.99 and default=0.0', max_digits=12)),
                ('total_tax', models.DecimalField(decimal_places=2, default=0.0, help_text='Total tax can have max value upto=9999999999.99 and default=0.0', max_digits=12)),
                ('grand_total', models.DecimalField(decimal_places=2, default=0.0, help_text='Grand total can have max value upto=9999999999.99 and default=0.0', max_digits=12)),
                ('branch', models.CharField(max_length=255)),
                ('remarks', models.CharField(blank=True, help_text='Remarks should be max. of 100 characters and blank=True', max_length=100)),
                ('return_dropped', models.BooleanField(default=True, help_text='True if items are dropped to locations after returning')),
                ('active', models.BooleanField(default=True, help_text='By default active=True')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('discount_scheme', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core_app.discountscheme')),
                ('fiscal_session_ad', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core_app.fiscalsessionad')),
                ('fiscal_session_bs', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core_app.fiscalsessionbs')),
                ('ref_transfer_master', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='transfer.transfermaster')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TransferDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date_ad', models.DateTimeField()),
                ('created_date_bs', models.CharField(max_length=10)),
                ('device_type', models.PositiveBigIntegerField(choices=[(1, 'Mobile'), (2, 'PC'), (3, 'Tablet'), (4, 'Other'), (5, 'NA')], default=5, help_text='where 1=Mobile, 2=PC, 3=Tablet and 4=Other')),
                ('app_type', models.PositiveBigIntegerField(choices=[(1, 'Web-App'), (2, 'IOS-App'), (3, 'Android-App'), (4, 'NA')], default=4, help_text='where 1=Web-App, 2=IOS-APP, 3=Android-APP')),
                ('cost', models.DecimalField(decimal_places=2, default=0.0, help_text='cost can have max value upto=9999999999.99 and default=0.0', max_digits=12)),
                ('qty', models.DecimalField(decimal_places=2, help_text='Purchase quantity can have max value upto=9999999999.99 and min_value=0.0', max_digits=12)),
                ('pack_qty', models.DecimalField(decimal_places=2, help_text="pack quantity can't be negative", max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('taxable', models.BooleanField(default=True, help_text='Check if item is taxable')),
                ('tax_rate', models.DecimalField(decimal_places=2, default=0.0, help_text='Tax rate if item is taxable, max_value=100.00 and default=0.0', max_digits=5)),
                ('tax_amount', models.DecimalField(decimal_places=2, default=0.0, help_text='Tax amount can have max value upto=9999999999.99 and default=0.0', max_digits=12)),
                ('discountable', models.BooleanField(default=True, help_text='Check if item is discountable')),
                ('discount_rate', models.DecimalField(decimal_places=2, default=0.0, help_text='Discount rate if item is discountable, max_value=100.00 and default=0.0', max_digits=5)),
                ('discount_amount', models.DecimalField(decimal_places=2, default=0.0, help_text='Discount amount can have max value upto=9999999999.99 and default=0.0', max_digits=12)),
                ('gross_amount', models.DecimalField(decimal_places=2, default=0.0, help_text='Gross amount can have max value upto=9999999999.99 and default=0.0', max_digits=12)),
                ('net_amount', models.DecimalField(decimal_places=2, default=0.0, help_text='Net amount can have max value upto=9999999999.99 and default=0.0', max_digits=12)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('item', models.ForeignKey(default=False, on_delete=django.db.models.deletion.PROTECT, to='item.item')),
                ('item_category', models.ForeignKey(default=False, on_delete=django.db.models.deletion.PROTECT, to='item.itemcategory')),
                ('ref_purchase_detail', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transfer_purchase_details', to='purchase.purchasedetail')),
                ('ref_transfer_detail', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='transfer.transferdetail')),
                ('transfer_master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transfer_details', to='transfer.transfermaster')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]