# Generated by Django 3.2 on 2022-06-13 05:00

from django.db import migrations, models
import django.db.models.deletion
import simple_history.models
import src.custom_lib.functions.field_value_validation


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0005_alter_item_basic_info'),
        ('customer', '0003_customer_user'),
        ('log_app', '0042_auto_20220612_1545'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogQuotationMaster',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('history_date_bs', models.CharField(blank=True, max_length=10, null=True)),
                ('device_type', models.PositiveBigIntegerField(choices=[(1, 'Mobile'), (2, 'PC'), (3, 'Tablet'), (4, 'Other'), (5, 'NA')], default=5, help_text='where 1=Mobile, 2=PC, 3=Tablet and 4=Other')),
                ('app_type', models.PositiveBigIntegerField(choices=[(1, 'Web-App'), (2, 'IOS-App'), (3, 'Android-App'), (4, 'NA')], default=4, help_text='where 1=Web-App, 2=IOS-APP, 3=Android-APP')),
                ('quotation_no', models.CharField(db_index=True, help_text='Quotation Id should be max. of 13 characters', max_length=20)),
                ('delivery_date_ad', models.DateField(blank=True, help_text='Bill Date AD', max_length=10, null=True)),
                ('delivery_date_bs', models.CharField(blank=True, help_text='Bill Date BS', max_length=10)),
                ('delivery_location', models.CharField(blank=True, help_text='Location should be max. of 100 characters', max_length=100)),
                ('remarks', models.CharField(blank=True, help_text='Remarks should be max. of 100 characters', max_length=100)),
                ('history_user_id', models.IntegerField(null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('customer', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='customer.customer')),
            ],
            options={
                'verbose_name': 'historical quotation master',
                'db_table': 'quotation_quotationmaster_log',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='LogQuotationDetail',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('history_date_bs', models.CharField(blank=True, max_length=10, null=True)),
                ('device_type', models.PositiveBigIntegerField(choices=[(1, 'Mobile'), (2, 'PC'), (3, 'Tablet'), (4, 'Other'), (5, 'NA')], default=5, help_text='where 1=Mobile, 2=PC, 3=Tablet and 4=Other')),
                ('app_type', models.PositiveBigIntegerField(choices=[(1, 'Web-App'), (2, 'IOS-App'), (3, 'Android-App'), (4, 'NA')], default=4, help_text='where 1=Web-App, 2=IOS-APP, 3=Android-APP')),
                ('qty', models.DecimalField(decimal_places=2, max_digits=12, validators=[src.custom_lib.functions.field_value_validation.gt_zero_validator])),
                ('sale_cost', models.DecimalField(decimal_places=2, default=0.0, help_text='sale cost of order default=0.00', max_digits=12)),
                ('remarks', models.CharField(blank=True, max_length=50)),
                ('history_user_id', models.IntegerField(null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('item', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='item.item')),
                ('item_category', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='item.itemcategory')),
            ],
            options={
                'verbose_name': 'historical quotation detail',
                'db_table': 'quotation_quotationdetail_log',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
