# Generated by Django 3.2 on 2022-05-05 06:47

from django.db import migrations, models
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        ('log_app', '0024_auto_20220505_1217'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogCurrency',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('history_date_bs', models.CharField(blank=True, max_length=10, null=True)),
                ('device_type', models.PositiveBigIntegerField(choices=[(1, 'Mobile'), (2, 'PC'), (3, 'Tablet'), (4, 'Other'), (5, 'NA')], default=5, help_text='where 1=Mobile, 2=PC, 3=Tablet and 4=Other')),
                ('app_type', models.PositiveBigIntegerField(choices=[(1, 'Web-App'), (2, 'IOS-App'), (3, 'Android-App'), (4, 'NA')], default=4, help_text='where 1=Web-App, 2=IOS-APP, 3=Android-APP')),
                ('name', models.CharField(blank=True, help_text='currency_name can be have max upto 50 characters and null=True, blank=True', max_length=50, null=True)),
                ('symbol', models.CharField(blank=True, help_text='currency_symbol can be have max upto 3 characters and null=True, blank=True', max_length=3, null=True)),
                ('code', models.CharField(blank=True, help_text='currency_name can be have max upto 3 characters and null=True, blank=True', max_length=3, null=True)),
                ('history_user_id', models.IntegerField(null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical currency',
                'db_table': 'core_app_currency_log',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
