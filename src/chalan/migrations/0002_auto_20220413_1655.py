# Generated by Django 3.1 on 2022-04-13 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chalan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chalanmaster',
            name='status',
            field=models.PositiveIntegerField(choices=[(1, 'CHALAN'), (2, 'BILLED'), (3, 'RETURNED')], help_text='Where 1 = CHALAN, 2 = BILLED,  3 = RETURNED, Default=1'),
        ),
    ]
