# Generated by Django 3.2 on 2022-06-13 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotationdetail',
            name='cancelled',
            field=models.BooleanField(default=False),
        ),
    ]
