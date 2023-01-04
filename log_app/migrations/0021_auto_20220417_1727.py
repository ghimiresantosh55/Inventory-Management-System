# Generated by Django 3.1 on 2022-04-17 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chalan', '0002_auto_20220413_1655'),
        ('log_app', '0020_auto_20220413_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='logsaledetail',
            name='ref_chalan_detail',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='chalan.chalandetail'),
        ),
        migrations.AddField(
            model_name='logsalemaster',
            name='ref_chalan_master',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='chalan.chalanmaster'),
        ),
    ]
