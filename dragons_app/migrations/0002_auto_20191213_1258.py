# Generated by Django 2.2 on 2019-12-13 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dragons_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dragonkillrecord',
            name='kill_time',
            field=models.CharField(max_length=255),
        ),
    ]
