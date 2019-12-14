from rest_framework import serializers

from dragons_app import models


class RuleSerializer(serializers.ModelSerializer):
    """Serializer for Rule Model"""
    class Meta:
        model = models.Rule
        fields = '__all__'


class DragonSerializer(serializers.ModelSerializer):
    """Serializer for Dragon Model"""
    class Meta:
        model = models.Dragon
        fields = '__all__'


class KillDragonSerializer(serializers.ModelSerializer):
    """Serializer for DragonKillRecord"""
    class Meta:
        model = models.DragonKillRecord
        fields = '__all__'
