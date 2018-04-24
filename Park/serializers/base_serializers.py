# Third-Party
from rest_framework import serializers

# Django
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

# Local Django
from Users.models import User
from Park.models import Park
from Core.models import City
from Core.serializers import CitySerializer


class ParkSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    creat_time = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    #number_of_car_inside
    #coordinate
    class Meta:
        model = Park
        fields = ('id', 'city', 'name', 'adress', 'capacity', 'number_of_car_inside', 'creat_time', 'coordinate')

class ParkListSerializer(ParkSerializer):

    class Meta:
        model = Park
        fields = ('id', 'name', 'capacity', 'number_of_car_inside',)


class ParkRetrieveSerializer(ParkSerializer):
    pass


class ParkCreateSerializer(ParkSerializer):

    class Meta:
        model = Park
        fields = ('city', 'name', 'address', 'capacity', 'coordinate')


class ParkUpdateSerializer(ParkSerializer):
    #number_of_car_inside
    class Meta:
        model = Park
        fields = ('name', 'address', 'coordinate', 'capacity')
