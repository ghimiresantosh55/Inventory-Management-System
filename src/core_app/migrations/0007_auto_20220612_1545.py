# Generated by Django 3.2 on 2022-06-12 10:00

from django.db import migrations, models
import src.core_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0006_auto_20220612_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationsetup',
            name='favicon',
            field=models.ImageField(blank=True, null=True, upload_to='organization_setup/favicon', validators=[src.core_app.models.validate_image]),
        ),
        migrations.AlterField(
            model_name='organizationsetup',
            name='signature',
            field=models.ImageField(blank=True, help_text='signature image of organization owner', null=True, upload_to='organization_setup/signature', validators=[src.core_app.models.validate_image]),
        ),
    ]