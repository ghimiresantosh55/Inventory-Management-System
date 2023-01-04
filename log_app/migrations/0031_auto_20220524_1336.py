# Generated by Django 3.2 on 2022-05-24 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_app', '0030_alter_loguser_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logitem',
            name='basic_info',
            field=models.TextField(blank=True, help_text='Basic info can text field', null=True),
        ),
        migrations.AlterField(
            model_name='logsupplier',
            name='address',
            field=models.TextField(blank=True, help_text='Address can be  text field and blank = True'),
        ),
    ]
