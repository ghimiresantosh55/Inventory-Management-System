# Generated by Django 3.2 on 2022-05-09 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_app', '0027_logcurrency_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='logitem',
            name='harmonic_code',
            field=models.CharField(blank=True, help_text='harmonic code max length 50', max_length=50),
        ),
    ]
