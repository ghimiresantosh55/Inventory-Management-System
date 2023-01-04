from django.db import migrations, models
import django.db.models.deletion
import simple_history.models
import src.core_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0016_purchaseorderdetail_remarks'),
        ('log_app', '0035_logpurchaseorderdetail_remarks'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogPurchaseDocumentType',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('history_date_bs', models.CharField(blank=True, max_length=10, null=True)),
                ('device_type', models.PositiveBigIntegerField(choices=[(1, 'Mobile'), (2, 'PC'), (3, 'Tablet'), (4, 'Other'), (5, 'NA')], default=5, help_text='where 1=Mobile, 2=PC, 3=Tablet and 4=Other')),
                ('app_type', models.PositiveBigIntegerField(choices=[(1, 'Web-App'), (2, 'IOS-App'), (3, 'Android-App'), (4, 'NA')], default=4, help_text='where 1=Web-App, 2=IOS-APP, 3=Android-APP')),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('active', models.BooleanField(default=True)),
                ('history_user_id', models.IntegerField(null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical purchase document type',
                'db_table': 'purchase_purchasedocumenttype_log',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='LogPurchaseDocument',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('history_date_bs', models.CharField(blank=True, max_length=10, null=True)),
                ('device_type', models.PositiveBigIntegerField(choices=[(1, 'Mobile'), (2, 'PC'), (3, 'Tablet'), (4, 'Other'), (5, 'NA')], default=5, help_text='where 1=Mobile, 2=PC, 3=Tablet and 4=Other')),
                ('app_type', models.PositiveBigIntegerField(choices=[(1, 'Web-App'), (2, 'IOS-App'), (3, 'Android-App'), (4, 'NA')], default=4, help_text='where 1=Web-App, 2=IOS-APP, 3=Android-APP')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('document_url', models.TextField(max_length=100, validators=[src.core_app.models.validate_image])),
                ('remarks', models.CharField(blank=True, help_text='maxlength = 100', max_length=100)),
                ('history_user_id', models.IntegerField(null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('purchase_document_type', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='purchase.purchasedocumenttype')),
                ('purchase_main', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='purchase.purchasemaster')),
            ],
            options={
                'verbose_name': 'historical purchase document',
                'db_table': 'purchase_purchasedocument_log',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
