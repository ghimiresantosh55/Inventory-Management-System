# Generated by Django 3.1 on 2022-02-27 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_app', '0003_logcustomgroup_remarks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logpurchaseordermaster',
            name='order_type',
            field=models.PositiveIntegerField(choices=[(1, 'ORDER'), (2, 'CANCELLED'), (3, 'RECEIVED'), (4, 'VERIFIED')], help_text='Order type like Order, approved, cancelled'),
        ),
    ]
