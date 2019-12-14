import datetime

from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from dragons_app import models, serializers
from dragons_app.utils import is_allowed_to_kill


class RuleView(APIView):
    """This API dragon_api/rules is allowed to create and view the rules"""
    # TokenAuthentication and permission class can be used to allow only the queen to create rules

    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = serializers.RuleSerializer

    def get(self, request):
        try:
            rules = models.Rule.objects.all()
            rule_serialized = self.serializer_class(rules, many=True)
            response = {
                'rules': rule_serialized.data,
                'status': status.HTTP_200_OK
            }
        except Exception as e:
            response = {
                'status': status.HTTP_500_INTERNAL_SERVER_ERROR
            }
        return Response(response)

    def post(self, request):
        request_deserialized = self.serializer_class(data=request.data)
        if request_deserialized.is_valid():
            # checking whether the new rule already exists
            time_period = request_deserialized.validated_data.get('time_period')
            max_animals_to_kill = request_deserialized.validated_data.get('max_animals_to_kill')
            if models.Rule.objects.filter(time_period=time_period).filter(
                    max_animals_to_kill=max_animals_to_kill).exists():
                response = {
                    'message': 'The Rule already exists',
                    'status': status.HTTP_200_OK
                }
            else:
                saved_rule = request_deserialized.save()
                response = {
                    'message': 'The Rule is sucessfully created',
                    'rule_id': saved_rule.__dict__.get('rule_id'),
                    'status': status.HTTP_201_CREATED,
                }
        else:
            response = {
                'message': 'Please provide valid input',
                'Errors': request_deserialized.errors,
                'status': status.HTTP_400_BAD_REQUEST

            }
        return Response(response)


class DeleteRuleView(APIView):
    """This API /dragon_api/delete-rule/<rule_id> is used to Delete Rule with rule_id"""
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    def delete(self, request, pk, format=None):
        rule = models.Rule.objects.filter(rule_id=pk)
        if rule.exists():
            rule.delete()
            response = {
                "message": f"The Rule with {pk} succesfully deleted",
                "status": status.HTTP_200_OK
            }
        else:
            response = {
                "message": f" The Rule with {pk} doesnot exists",
                "status": status.HTTP_400_BAD_REQUEST
            }

        return Response(response)


class DragonView(APIView):
    """This API /dragon_api/dragons is used to register dragon and view the dragons"""
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = serializers.DragonSerializer

    def get(self, request):
        try:
            dragons = models.Dragon.objects.all()
            dragons_serialized = self.serializer_class(dragons, many=True)
            response = {
                'rules': dragons_serialized.data,
                'status': status.HTTP_200_OK
            }
        except Exception as e:
            response = {
                'status': status.HTTP_500_INTERNAL_SERVER_ERROR
            }
        return Response(response)

    def post(self, request):
        request_deserialized = self.serializer_class(data=request.data)
        if request_deserialized.is_valid():
            # checking whether the dragon_name already exists
            dragon_name = request_deserialized.validated_data.get('dragon_name')
            if models.Dragon.objects.filter(dragon_name=dragon_name).exists():
                response = {
                    'message': 'The Dragon name already exists',
                    'status': status.HTTP_200_OK
                }
            else:
                saved_dragon = request_deserialized.save()
                response = {
                    'message': 'The Dragon is sucessfully registered',
                    'dragon_id': saved_dragon.__dict__.get('dragon_id'),
                    'status': status.HTTP_201_CREATED,
                }
        else:
            response = {
                'message': 'Please provide valid input',
                'Errors': request_deserialized.errors,
                'status': status.HTTP_400_BAD_REQUEST

            }
        return Response(response)


@api_view(['POST'])
def kill_by_dragon(request):
    """This API /dragon_api/kill_by_dragon is used to Request to kill animal"""
    kill_dragon_deserialized = serializers.KillDragonSerializer(data=request.data)
    if kill_dragon_deserialized.is_valid():
        kill_time_string = kill_dragon_deserialized.validated_data.get('kill_time')
        dragon = kill_dragon_deserialized.validated_data.get('dragon')
        animals_to_kill = kill_dragon_deserialized.validated_data.get('animals_killed')
        try:
            kill_time = datetime.datetime.strptime(kill_time_string, "%Y-%m-%d-%H:%M")

        except ValueError as ve:
            raise Exception()
        is_allowed = is_allowed_to_kill(dragon,kill_time,animals_to_kill)
        if is_allowed:
            response ={
                'did kill': is_allowed
            }
            kill_dragon_deserialized.save()
        else:
            response = {
                'did kill': is_allowed
            }


    else:
        response = {
            'Error': kill_dragon_deserialized.errors
        }
    return Response(response)
