# Generated by Django 3.2 on 2022-05-05 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_app', '0026_alter_logitem_basic_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='logcurrency',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
