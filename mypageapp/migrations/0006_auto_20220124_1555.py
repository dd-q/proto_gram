# Generated by Django 3.2.5 on 2022-01-24 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypageapp', '0005_pet_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_addr',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(max_length=50),
        ),
    ]
