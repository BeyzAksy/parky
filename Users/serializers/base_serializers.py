# Third-Party
from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _

# Django
from django.conf import settings
from django.contrib.auth import password_validation

# Local Django
from user.models import User
from core.models import City
from core.serializers import CitySerializer, CityListSerializer

class UserSerializer(serializers.ModelSerializer):
    try:
        city = City.objects.get(user_id=id)
        serializer = CitySerializer(many=True, read_only=True)
    except:
        pass

    class Meta:
        model = User
        fields = (
            'id', 'email', 'first_name', 'city', 'last_name', 'is_active',
        )


class UserListSerializer(UserSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'city',)
