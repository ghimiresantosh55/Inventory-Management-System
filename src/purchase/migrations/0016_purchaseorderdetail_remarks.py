# Generated by Django 3.2 on 2022-05-25 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0015_purchaseorderdetail_cancelled'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseorderdetail',
            name='remarks',
            field=models.TextField(blank=True, null=True),
        ),
    ]
