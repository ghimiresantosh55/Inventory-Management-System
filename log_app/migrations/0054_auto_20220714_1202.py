# Generated by Django 3.2 on 2022-07-14 06:17

import django.core.validators
from django.db import migrations, models
import src.core_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('log_app', '0053_alter_logpurchasedetail_batch_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logorganizationsetup',
            name='favicon',
            field=models.TextField(blank=True, default='default_images/favicon.ico', max_length=100, null=True, validators=[src.core_app.models.validate_image]),
        ),
        migrations.AlterField(
            model_name='logorganizationsetup',
            name='logo',
            field=models.TextField(blank=True, default='default_images/soori.png', max_length=100, validators=[src.core_app.models.validate_image, django.core.validators.FileExtensionValidator(allowed_extensions=['png'])]),
        ),
        migrations.AlterField(
            model_name='logorganizationsetup',
            name='signature',
            field=models.TextField(blank=True, default='default_images/signature.png', help_text='signature image of organization owner', max_length=100, null=True, validators=[src.core_app.models.validate_image]),
        ),
        migrations.AlterField(
            model_name='logorganizationsetup',
            name='stamp',
            field=models.TextField(blank=True, default='default_images/stamp.png', help_text='stamp image of organization', max_length=100, validators=[src.core_app.models.validate_image]),
        ),
    ]
