# Generated by Django 3.2 on 2022-05-25 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_app', '0033_alter_logpurchaseordermaster_attendee'),
    ]

    operations = [
        migrations.AddField(
            model_name='logpurchaseorderdetail',
            name='cancelled',
            field=models.BooleanField(default=False),
        ),
    ]
