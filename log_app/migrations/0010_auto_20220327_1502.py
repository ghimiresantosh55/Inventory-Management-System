# Generated by Django 3.1 on 2022-03-27 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_app', '0009_logorderdetail_item_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logpurchasemaster',
            name='pay_type',
            field=models.PositiveIntegerField(choices=[(1, 'CASH'), (2, 'CREDIT')], help_text='Pay type like CASH, CREDIT or PARTIAL'),
        ),
    ]
