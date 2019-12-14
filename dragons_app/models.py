from django.db import models


# Create your models here.

class Rule(models.Model):
    rule_id = models.AutoField(primary_key=True)
    time_period = models.IntegerField()
    max_animals_to_kill = models.IntegerField()


class Dragon(models.Model):
    dragon_id = models.AutoField(primary_key=True)
    dragon_name = models.CharField(max_length=255)


class DragonKillRecord(models.Model):
    dragon = models.ForeignKey(Dragon, on_delete=models.CASCADE)
    kill_time = models.CharField(max_length=255)
    animals_killed = models.IntegerField()
