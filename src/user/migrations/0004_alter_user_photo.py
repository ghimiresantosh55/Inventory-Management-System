# Generated by Django 3.2 on 2022-07-15 04:35

from django.db import migrations, models
import src.user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, default='default_images/profile.png', upload_to=src.user.models.upload_path_user, validators=[src.user.models.validate_image]),
        ),
    ]