# Generated by Django 3.2 on 2022-11-13 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0007_alter_item_image'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='packingtypedetail',
            unique_together={('item', 'packing_type', 'pack_qty')},
        ),
    ]
