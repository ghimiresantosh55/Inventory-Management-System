# Generated by Django 3.2 on 2022-06-20 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_app', '0047_alter_logquotationdetail_qty'),
    ]

    operations = [
        migrations.AddField(
            model_name='logordermaster',
            name='by_batch',
            field=models.BooleanField(default=False, help_text='True if customer order is placed batch wise, False if customer order is placed according to FIFO'),
        ),
    ]
