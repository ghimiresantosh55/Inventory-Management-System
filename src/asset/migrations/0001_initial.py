# Generated by Django 3.1 on 2022-02-15 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssetIssue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date_ad', models.DateTimeField()),
                ('created_date_bs', models.CharField(max_length=10)),
                ('device_type', models.PositiveBigIntegerField(choices=[(1, 'Mobile'), (2, 'PC'), (3, 'Tablet'), (4, 'Other'), (5, 'NA')], default=5, help_text='where 1=Mobile, 2=PC, 3=Tablet and 4=Other')),
                ('app_type', models.PositiveBigIntegerField(choices=[(1, 'Web-App'), (2, 'IOS-App'), (3, 'Android-App'), (4, 'NA')], default=4, help_text='where 1=Web-App, 2=IOS-APP, 3=Android-APP')),
                ('issue_type', models.PositiveIntegerField(choices=[(1, 'ISSUED'), (2, 'RETURNED')], help_text='Order type like Issued, Returned')),
                ('due_date_ad', models.DateField(help_text='Due Date AD')),
                ('due_date_bs', models.CharField(help_text='Due Date BS', max_length=10)),
                ('return_date_ad', models.DateField(blank=True, help_text='Due Date AD', null=True)),
                ('return_date_bs', models.CharField(blank=True, help_text='Due Date BS', max_length=10)),
                ('remarks', models.CharField(blank=True, help_text='Remarks should be max. of 100 characters', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AssetList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date_ad', models.DateTimeField()),
                ('created_date_bs', models.CharField(max_length=10)),
                ('device_type', models.PositiveBigIntegerField(choices=[(1, 'Mobile'), (2, 'PC'), (3, 'Tablet'), (4, 'Other'), (5, 'NA')], default=5, help_text='where 1=Mobile, 2=PC, 3=Tablet and 4=Other')),
                ('app_type', models.PositiveBigIntegerField(choices=[(1, 'Web-App'), (2, 'IOS-App'), (3, 'Android-App'), (4, 'NA')], default=4, help_text='where 1=Web-App, 2=IOS-APP, 3=Android-APP')),
                ('scrapped', models.BooleanField(default=False, help_text='default = False')),
                ('available', models.BooleanField(default=True, help_text='default = True')),
                ('remarks', models.CharField(blank=True, help_text='Remarks should be max. of 100 characters', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AssetService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date_ad', models.DateTimeField()),
                ('created_date_bs', models.CharField(max_length=10)),
                ('device_type', models.PositiveBigIntegerField(choices=[(1, 'Mobile'), (2, 'PC'), (3, 'Tablet'), (4, 'Other'), (5, 'NA')], default=5, help_text='where 1=Mobile, 2=PC, 3=Tablet and 4=Other')),
                ('app_type', models.PositiveBigIntegerField(choices=[(1, 'Web-App'), (2, 'IOS-App'), (3, 'Android-App'), (4, 'NA')], default=4, help_text='where 1=Web-App, 2=IOS-APP, 3=Android-APP')),
                ('service_status', models.PositiveIntegerField(choices=[(1, 'PENDING'), (2, 'REPAIRED')], help_text='Status like PENDING, REPAIRED')),
                ('receive_date_ad', models.DateField(blank=True, help_text='Due Date AD', null=True)),
                ('receive_date_bs', models.CharField(blank=True, help_text='Due Date BS', max_length=10, null=True)),
                ('taken_by', models.CharField(blank=True, help_text='Taken by should be max. of 50 characters', max_length=50)),
                ('problem', models.CharField(blank=True, help_text='Problem should be max. of 100 characters', max_length=100)),
                ('solution', models.CharField(blank=True, help_text='Solution should be max. of 100 characters', max_length=100)),
                ('remarks', models.CharField(blank=True, help_text='Remarks should be max. of 100 characters', max_length=100)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='asset.assetlist')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
