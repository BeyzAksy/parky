# Third-Party
from rest_framework import serializers

# Django
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

# Local Django
from Users.models import User
from Car.models import Car


class CarSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source="get_type_display")

    class Meta:
        model = Car
        fields = ('id', 'plate', 'color', 'type')


class CarListSerializer(CarSerializer):

    class Meta:
        model = Car
        fields = ('id', 'plate', 'type')


class CarRetrieveSerializer(CarSerializer):
    pass


class CarCreateSerializer(CarSerializer):

    class Meta:
        model = Car
        fields = ('plate', 'color', 'type')


class CarUpdateSerializer(CarSerializer):

    class Meta:
        model = Car
        fields = ('plate', 'color')
