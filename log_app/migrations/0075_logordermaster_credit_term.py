# Generated by Django 3.2 on 2022-12-05 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_app', '0074_logcustomer_credit_limit'),
    ]

    operations = [
        migrations.AddField(
            model_name='logordermaster',
            name='credit_term',
            field=models.PositiveIntegerField(blank=True, default=30, null=True),
        ),
    ]