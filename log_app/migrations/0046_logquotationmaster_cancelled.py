# Generated by Django 3.2 on 2022-06-13 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_app', '0045_logquotationdetail_cancelled'),
    ]

    operations = [
        migrations.AddField(
            model_name='logquotationmaster',
            name='cancelled',
            field=models.BooleanField(default=False),
        ),
    ]
