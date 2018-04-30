# Third-Party
from rest_framework import serializers

# Django
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

# Local Django
from Users.models import User
from Rezervation.models import Rezervation
from Car.models import Car
from Park.models import Park
from Car.serializers import CarSerializer
from Park.serializers import ParkSerializer


class RezervationSerializer(serializers.ModelSerializer):
    try:
        park = Park.objects.get(user_id=id)
        serializer = ParkSerializer(many=True, read_only=True)
    except:
        pass

    try:
        car = Car.objects.get(user_id=id)
        serializer = CarSerializer(many=True, read_only=True)
    except:
        pass

    #car = CarSerializer()
    start_time = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    end_time = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")

    class Meta:
        model = Rezervation
        fields = ('id', 'park', 'car', 'start_time', 'end_time')

class RezervationListSerializer(RezervationSerializer):

    class Meta:
        model = Rezervation
        fields = ('id', 'park', 'car', 'start_time', 'end_time',)


class RezervationRetrieveSerializer(RezervationSerializer):
    pass


class RezervationCreateSerializer(RezervationSerializer):

    def __init__(self, *args, **kwargs):
        super(RezervationCreateSerializer, self).__init__(*args, **kwargs)
        request_user = self.context['request'].user
        self.fields['car'].queryset = Car.objects.filter(user=request_user)

    class Meta:
        model = Rezervation
        fields = ('park','car', 'start_time', 'end_time',)


class RezervationUpdateSerializer(RezervationSerializer):

    class Meta:
        model = Rezervation
        fields = ( 'start_time', 'end_time')
