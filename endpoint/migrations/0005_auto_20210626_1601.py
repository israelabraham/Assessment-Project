# Generated by Django 3.2.4 on 2021-06-26 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endpoint', '0004_alter_user_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]