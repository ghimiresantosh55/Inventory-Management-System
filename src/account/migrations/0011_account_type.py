# Generated by Django 3.2 on 2022-11-30 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_vouchermaster_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='type',
            field=models.CharField(default='ACCOUNT', max_length=100, verbose_name=[('ACCOUNT', 'ACCOUNT'), ('CUSTOMER', 'CUSTOMER'), ('SUPPLIER', 'SUPPLIER')]),
        ),
    ]
