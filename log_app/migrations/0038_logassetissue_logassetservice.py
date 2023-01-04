# Generated by Django 3.2 on 2022-05-27 04:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0007_auto_20220403_1418'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('log_app', '0037_logpurchaseorderdocument'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogAssetService',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('history_date_bs', models.CharField(blank=True, max_length=10, null=True)),
                ('device_type', models.PositiveBigIntegerField(choices=[(1, 'Mobile'), (2, 'PC'), (3, 'Tablet'), (4, 'Other'), (5, 'NA')], default=5, help_text='where 1=Mobile, 2=PC, 3=Tablet and 4=Other')),
                ('app_type', models.PositiveBigIntegerField(choices=[(1, 'Web-App'), (2, 'IOS-App'), (3, 'Android-App'), (4, 'NA')], default=4, help_text='where 1=Web-App, 2=IOS-APP, 3=Android-APP')),
                ('service_status', models.PositiveIntegerField(choices=[(1, 'PENDING'), (2, 'REPAIRED')], help_text='Status like PENDING, REPAIRED')),
                ('receive_date_ad', models.DateField(blank=True, help_text='Due Date AD', null=True)),
                ('receive_date_bs', models.CharField(blank=True, help_text='Due Date BS', max_length=10, null=True)),
                ('solution', models.CharField(blank=True, help_text='Solution should be max. of 100 characters', max_length=100)),
                ('taken_by', models.CharField(blank=True, help_text='Taken by should be max. of 50 characters', max_length=50)),
                ('problem', models.CharField(blank=True, help_text='Problem should be max. of 100 characters', max_length=100)),
                ('remarks', models.CharField(blank=True, help_text='Remarks should be max. of 100 characters', max_length=100)),
                ('history_user_id', models.IntegerField(null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('asset', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='asset.assetlist')),
            ],
            options={
                'verbose_name': 'historical asset service',
                'db_table': 'asset_assetservice_log',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='LogAssetIssue',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('history_date_bs', models.CharField(blank=True, max_length=10, null=True)),
                ('device_type', models.PositiveBigIntegerField(choices=[(1, 'Mobile'), (2, 'PC'), (3, 'Tablet'), (4, 'Other'), (5, 'NA')], default=5, help_text='where 1=Mobile, 2=PC, 3=Tablet and 4=Other')),
                ('app_type', models.PositiveBigIntegerField(choices=[(1, 'Web-App'), (2, 'IOS-App'), (3, 'Android-App'), (4, 'NA')], default=4, help_text='where 1=Web-App, 2=IOS-APP, 3=Android-APP')),
                ('issue_type', models.PositiveIntegerField(choices=[(1, 'ISSUED'), (2, 'RETURNED')], help_text='Order type like Issued, Returned')),
                ('due_date_ad', models.DateField(help_text='Due Date AD')),
                ('due_date_bs', models.CharField(help_text='Due Date BS', max_length=10)),
                ('return_date_ad', models.DateField(blank=True, help_text='Due Date AD', null=True)),
                ('return_date_bs', models.CharField(blank=True, help_text='Due Date BS', max_length=10)),
                ('remarks', models.CharField(blank=True, help_text='Remarks should be max. of 100 characters', max_length=100)),
                ('history_user_id', models.IntegerField(null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('asset', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='asset.assetlist')),
                ('issued_to', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('return_received_by', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical asset issue',
                'db_table': 'asset_assetissue_log',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
