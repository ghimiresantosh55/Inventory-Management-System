# Generated by Django 3.2 on 2022-06-12 07:07

from django.db import migrations, models
import src.core_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('log_app', '0040_alter_logpurchaseorderdetail_sale_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='logorganizationsetup',
            name='signature',
            field=models.TextField(blank=True, help_text='signature image of organization owner', max_length=100, validators=[src.core_app.models.validate_image]),
        ),
        migrations.AddField(
            model_name='logorganizationsetup',
            name='stamp',
            field=models.TextField(blank=True, help_text='stamp image of organization', max_length=100, validators=[src.core_app.models.validate_image]),
        ),
    ]