# Generated by Django 3.2.5 on 2022-01-25 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypageapp', '0002_auto_20220125_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='age',
            field=models.DateField(blank=True, null=True),
        ),
    ]
