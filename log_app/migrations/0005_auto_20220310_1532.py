# Generated by Django 3.1 on 2022-03-10 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_app', '0004_auto_20220227_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logpurchasedetail',
            name='batch_no',
            field=models.CharField(help_text='Batch no. max length 20', max_length=8),
        ),
    ]
