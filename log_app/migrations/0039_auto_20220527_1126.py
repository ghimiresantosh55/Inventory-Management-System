# Generated by Django 3.2 on 2022-05-27 05:41

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0005_currency_active'),
        ('log_app', '0038_logassetissue_logassetservice'),
    ]

    operations = [
        migrations.AddField(
            model_name='logpurchaseordermaster',
            name='currency',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='Currency For Foreign exchange', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='core_app.currency'),
        ),
        migrations.AddField(
            model_name='logpurchaseordermaster',
            name='currency_exchange_rate',
            field=models.DecimalField(decimal_places=5, default=Decimal('0.00'), help_text='exchange rate max 10 digits with 5 decimal places', max_digits=10),
        ),
    ]
