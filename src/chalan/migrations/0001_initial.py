# Generated by Django 3.1 on 2022-04-13 09:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import src.custom_lib.functions.field_value_validation


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0003_customer_user'),
        ('core_app', '0002_auto_20220215_1257'),
        ('customer_order', '0006_ordermaster_pick_verified'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('item', '0002_auto_20220215_1257'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChalanMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date_ad', models.DateTimeField()),
                ('created_date_bs', models.CharField(max_length=10)),
                ('device_type', models.PositiveBigIntegerField(choices=[(1, 'Mobile'), (2, 'PC'), (3, 'Tablet'), (4, 'Other'), (5, 'NA')], default=5, help_text='where 1=Mobile, 2=PC, 3=Tablet and 4=Other')),
                ('app_type', models.PositiveBigIntegerField(choices=[(1, 'Web-App'), (2, 'IOS-App'), (3, 'Android-App'), (4, 'NA')], default=4, help_text='where 1=Web-App, 2=IOS-APP, 3=Android-APP')),
                ('chalan_no', models.CharField(help_text='Chalan No should be max. of 20 characters', max_length=20, unique=True)),
                ('status', models.PositiveIntegerField(choices=[(1, 'CHALAN'), (2, 'BILLED'), (3, 'CANCELLED')], help_text='Where 1 = CHALAN, 2 = BILLED,  3 = CANCELLED, Default=1')),
                ('total_discount', models.DecimalField(decimal_places=2, default=0.0, help_text='Total discount default=0.00', max_digits=12)),
                ('total_tax', models.DecimalField(decimal_places=2, default=0.0, help_text='Total tax default=0.00', max_digits=12)),
                ('sub_total', models.DecimalField(decimal_places=2, default=0.0, help_text='Sub total default=0.00', max_digits=12)),
                ('total_discountable_amount', models.DecimalField(decimal_places=2, default=0.0, help_text='Total discountable amount', max_digits=12)),
                ('total_taxable_amount', models.DecimalField(decimal_places=2, default=0.0, help_text='Total taxable amount', max_digits=12)),
                ('total_non_taxable_amount', models.DecimalField(decimal_places=2, default=0.0, help_text='Total nontaxable amount', max_digits=12)),
                ('grand_total', models.DecimalField(decimal_places=2, default=0.0, help_text='Grand total default=0.00', max_digits=12)),
                ('remarks', models.CharField(blank=True, help_text='Remarks should be max. of 100 characters', max_length=100)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customer.customer')),
                ('discount_scheme', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core_app.discountscheme')),
                ('order_master', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='customer_order.ordermaster')),
                ('ref_chalan_master', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='chalan.chalanmaster')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ChalanDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date_ad', models.DateTimeField()),
                ('created_date_bs', models.CharField(max_length=10)),
                ('device_type', models.PositiveBigIntegerField(choices=[(1, 'Mobile'), (2, 'PC'), (3, 'Tablet'), (4, 'Other'), (5, 'NA')], default=5, help_text='where 1=Mobile, 2=PC, 3=Tablet and 4=Other')),
                ('app_type', models.PositiveBigIntegerField(choices=[(1, 'Web-App'), (2, 'IOS-App'), (3, 'Android-App'), (4, 'NA')], default=4, help_text='where 1=Web-App, 2=IOS-APP, 3=Android-APP')),
                ('qty', models.DecimalField(decimal_places=2, max_digits=12, validators=[src.custom_lib.functions.field_value_validation.gt_zero_validator])),
                ('sale_cost', models.DecimalField(decimal_places=2, default=0.0, help_text='sale cost of order default=0.00', max_digits=12)),
                ('discountable', models.BooleanField(default=True, help_text='Check if item is discountable default=True')),
                ('taxable', models.BooleanField(default=True, help_text='Check if item is discountable default=True')),
                ('tax_rate', models.DecimalField(decimal_places=2, default=0.0, help_text='Tax rate if item is taxable, default=0.00 max upto 100.00', max_digits=5)),
                ('tax_amount', models.DecimalField(decimal_places=2, default=0.0, help_text='default = 0.00 ', max_digits=12)),
                ('discount_rate', models.DecimalField(decimal_places=2, default=0.0, help_text='Discount rate if item is discountable, default=0.00 and max upto 100.00', max_digits=5)),
                ('discount_amount', models.DecimalField(decimal_places=2, default=0.0, help_text='default = 0.00 ', max_digits=12)),
                ('gross_amount', models.DecimalField(decimal_places=2, default=0.0, help_text='default = 0.00 ', max_digits=12)),
                ('net_amount', models.DecimalField(decimal_places=2, default=0.0, help_text='default = 0.00 ', max_digits=12)),
                ('remarks', models.CharField(blank=True, max_length=50)),
                ('chalan_master', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='chalan_details', to='chalan.chalanmaster')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='item.item')),
                ('item_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='item.itemcategory')),
                ('order_detail', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='customer_order.orderdetail')),
                ('ref_chalan_detail', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='chalan.chalandetail')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]