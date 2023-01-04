# Generated by Django 3.1 on 2022-02-15 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PackingTypeCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date_ad', models.DateTimeField()),
                ('created_date_bs', models.CharField(max_length=10)),
                ('device_type', models.PositiveBigIntegerField(choices=[(1, 'Mobile'), (2, 'PC'), (3, 'Tablet'), (4, 'Other'), (5, 'NA')], default=5, help_text='where 1=Mobile, 2=PC, 3=Tablet and 4=Other')),
                ('app_type', models.PositiveBigIntegerField(choices=[(1, 'Web-App'), (2, 'IOS-App'), (3, 'Android-App'), (4, 'NA')], default=4, help_text='where 1=Web-App, 2=IOS-APP, 3=Android-APP')),
                ('code', models.CharField(help_text='max-20', max_length=20, unique=True, verbose_name='Packing Type Serial No')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PackingTypeDetailCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date_ad', models.DateTimeField()),
                ('created_date_bs', models.CharField(max_length=10)),
                ('device_type', models.PositiveBigIntegerField(choices=[(1, 'Mobile'), (2, 'PC'), (3, 'Tablet'), (4, 'Other'), (5, 'NA')], default=5, help_text='where 1=Mobile, 2=PC, 3=Tablet and 4=Other')),
                ('app_type', models.PositiveBigIntegerField(choices=[(1, 'Web-App'), (2, 'IOS-App'), (3, 'Android-App'), (4, 'NA')], default=4, help_text='where 1=Web-App, 2=IOS-APP, 3=Android-APP')),
                ('code', models.CharField(help_text='max-20', max_length=20, unique=True, verbose_name='Packing Type Detail Serail No')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SalePackingTypeCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('packing_type_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pack_type_code_of_sale', to='item_serialization.packingtypecode', verbose_name='sale packing type code')),
            ],
        ),
        migrations.CreateModel(
            name='SalePackingTypeDetailCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('packing_type_detail_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pack_type_detail_code_of_sale', to='item_serialization.packingtypedetailcode')),
                ('sale_packing_type_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sale_packing_type_detail_code', to='item_serialization.salepackingtypecode')),
            ],
        ),
    ]
