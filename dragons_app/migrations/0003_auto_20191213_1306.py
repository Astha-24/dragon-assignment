# Generated by Django 2.2 on 2019-12-13 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dragons_app', '0002_auto_20191213_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dragonkillrecord',
            name='kill_time',
            field=models.DateTimeField(),
        ),
    ]
