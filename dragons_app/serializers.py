from rest_framework import serializers

from dragons_app import models


class RuleSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Rule
        fields = '__all__'


class DragonSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Dragon
        fields = '__all__'


class KillDragonSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.DragonKillRecord
        fields = '__all__'
