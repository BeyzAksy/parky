from rest_framework import serializers

# Django
from django.utils.translation import ugettext_lazy as _

# Local Django
from Core.models import City

class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ('id', 'city',)


class CityListSerializer(CitySerializer):

    class Meta:
        model = City
        fields = ('city',)
