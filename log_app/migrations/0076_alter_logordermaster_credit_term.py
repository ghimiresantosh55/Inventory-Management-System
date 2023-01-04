# Generated by Django 3.2 on 2022-12-05 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_app', '0075_logordermaster_credit_term'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logordermaster',
            name='credit_term',
            field=models.PositiveIntegerField(blank=True, choices=[(15, '15 days'), (30, '30 days'), (45, '45 days'), (60, '60 days')], default=30, null=True),
        ),
    ]
