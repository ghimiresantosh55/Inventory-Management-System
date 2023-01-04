# Generated by Django 3.1 on 2022-02-15 07:12

from django.db import migrations, models
import django.db.models.deletion
import src.supplier.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date_ad', models.DateTimeField()),
                ('created_date_bs', models.CharField(max_length=10)),
                ('device_type', models.PositiveBigIntegerField(choices=[(1, 'Mobile'), (2, 'PC'), (3, 'Tablet'), (4, 'Other'), (5, 'NA')], default=5, help_text='where 1=Mobile, 2=PC, 3=Tablet and 4=Other')),
                ('app_type', models.PositiveBigIntegerField(choices=[(1, 'Web-App'), (2, 'IOS-App'), (3, 'Android-App'), (4, 'NA')], default=4, help_text='where 1=Web-App, 2=IOS-APP, 3=Android-APP')),
                ('name', models.CharField(help_text='First name can be max. of 150 characters', max_length=150)),
                ('address', models.CharField(blank=True, help_text='Address can be max. of 50 characters and blank = True', max_length=50)),
                ('phone_no', models.CharField(blank=True, help_text='Phone no. can be max. of 15 characters, blank=True', max_length=15)),
                ('mobile_no', models.CharField(blank=True, help_text='Mobile no. can be max. of 15 characters, blank=True', max_length=15)),
                ('email_id', models.CharField(blank=True, help_text='Email Id can be max. of 50 characters, blank=True', max_length=50)),
                ('tax_reg_system', models.PositiveIntegerField(choices=[(1, 'VAT'), (2, 'PAN')], default=1, help_text='by default=1')),
                ('pan_vat_no', models.CharField(blank=True, help_text='PAN can be max. of 15 characters, blank=True', max_length=9)),
                ('opening_balance', models.DecimalField(decimal_places=2, default=0.0, help_text='Max value opening_value can be upto 9999999999.99', max_digits=12)),
                ('image', models.ImageField(blank=True, help_text='max image size can be 2 MB', null=True, upload_to='supplier', validators=[src.supplier.models.validate_image])),
                ('active', models.BooleanField(default=True, help_text='by default active = True')),
                ('country', models.ForeignKey(blank=True, help_text='blank= True and null= True', null=True, on_delete=django.db.models.deletion.PROTECT, to='core_app.country')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
