# Generated by Django 2.2 on 2019-12-14 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dragons_app', '0004_auto_20191214_0327'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dragonkillrecord',
            old_name='animals_to_kill',
            new_name='animals_killed',
        ),
    ]