# Generated by Django 3.2 on 2022-07-07 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit_management', '0004_alter_creditclearance_sale_master'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditpaymentdetail',
            name='payment_id',
            field=models.CharField(blank=True, help_text='Payment Mode ID, Esewa No/Khalti No/Cheque No', max_length=255),
        ),
    ]
