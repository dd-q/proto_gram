# Generated by Django 3.2.5 on 2022-01-25 01:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mypageapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='user_id',
            field=models.ForeignKey(db_column='user_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='mypageapp.user', unique=True),
        ),
    ]