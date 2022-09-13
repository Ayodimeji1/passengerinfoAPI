from rest_framework import ModelSerializer
from Passenger import models


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = ['id','name', 'age', 'sex']
