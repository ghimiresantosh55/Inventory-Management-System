# Generated by Django 3.2 on 2022-12-05 09:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer_order', '0010_auto_20221205_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetail',
            name='picked_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='order_details_picked', to=settings.AUTH_USER_MODEL),
        ),
    ]
