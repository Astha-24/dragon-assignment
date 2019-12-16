from dragons_app import models, serializers
import datetime as dt

DATETIME_FORMAT = "%Y-%m-%d-%H:%M"


def is_allowed_to_kill(dragon, request_kill_time, request_animals_to_kill):
    """This function is used to check whether the kill request is allowed or not"""
    rules = models.Rule.objects.all().order_by('time_period')
    rules_serialized = serializers.RuleSerializer(rules, many=True)
    dragon_kill_records = models.DragonKillRecord.objects.filter(dragon=dragon).order_by('kill_time')
    dragon_kill_record_serialized = serializers.KillDragonSerializer(dragon_kill_records, many=True)
    end_time = request_kill_time

    for rule in rules_serialized.data:
        time_period = rule.get('time_period')
        max_animals_to_kill = rule.get('max_animals_to_kill')
        start_time = request_kill_time - dt.timedelta(hours=time_period)
        count_dragon_killed = 0
        for dragon_kill_record in dragon_kill_record_serialized.data:
            kill_time_record_string = dragon_kill_record.get('kill_time')
            kill_time_record = dt.datetime.strptime(kill_time_record_string, DATETIME_FORMAT)
            if start_time < kill_time_record <= end_time:
                count_dragon_killed += dragon_kill_record.get('animals_killed')
        if count_dragon_killed + request_animals_to_kill > max_animals_to_kill:
            return False
    return True
