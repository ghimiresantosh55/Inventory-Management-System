# Generated by Django 3.2 on 2022-11-30 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_account_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='code',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
