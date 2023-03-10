# Generated by Django 3.1 on 2022-04-18 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_app', '0021_auto_20220417_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='logchalanmaster',
            name='discount_rate',
            field=models.DecimalField(decimal_places=2, default=0.0, help_text='Discount rate if applicable, default=0.0 and max_value upto=100.00', max_digits=5),
        ),
    ]
