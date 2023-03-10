# Generated by Django 3.2 on 2022-07-01 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_app', '0048_logordermaster_by_batch'),
    ]

    operations = [
        migrations.AddField(
            model_name='logchalanmaster',
            name='return_dropped',
            field=models.BooleanField(default=True, help_text='True if items are dropped to locations after returning'),
        ),
        migrations.AddField(
            model_name='logsalemaster',
            name='return_dropped',
            field=models.BooleanField(default=True, help_text='True if items are dropped to locations after returning'),
        ),
    ]
