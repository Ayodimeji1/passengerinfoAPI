from rest_framework import serializers
from passenger.models import Passenger


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = ['id','first_name','last_name','arrival','departure']
