# Generated by Django 3.2 on 2022-09-29 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0002_alter_repairdetail_repair'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repair',
            name='expected_date_to_repair_ad',
            field=models.DateField(blank=True, help_text='Expected Date To Repair AD, blank = True', null=True),
        ),
        migrations.AlterField(
            model_name='repair',
            name='expected_date_to_repair_bs',
            field=models.CharField(blank=True, help_text='Expected Date To Repair BS, blank = True', max_length=10),
        ),
    ]