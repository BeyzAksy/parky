# Third-Party
from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _

# Django
from django.conf import settings
from django.contrib.auth import password_validation

# Local Django
from Users.models import User
from Core.models import City
from Core.serializers import CitySerializer, CityListSerializer

class UserSerializer(serializers.ModelSerializer):
    try:
        city = City.objects.get(user_id=id)
        serializer = CitySerializer(many=True, read_only=True)
    except:
        pass

    class Meta:
        model = User
        fields = (
            'id', 'email', 'first_name', 'last_name' , 'phone_number', 'city', 'is_active',
        )


class UserListSerializer(UserSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'phone_number', 'city',)

class UserRetrieveSerializer(UserSerializer):
    pass


class UserCreateSerializer(UserSerializer):
    confirm_password = serializers.CharField()

    class Meta:
        model = User
        fields = (
            'city', 'email', 'first_name', 'last_name', 'phone_number', 'password', 'confirm_password')
        extra_kwargs = {
            'password': {'write_only': True},
            'city': {'required': True}
        }

    def create(self, validated_data):
        del validated_data["confirm_password"]
        return super(UserCreateSerializer, self).create(validated_data)

    def validate_password(self, value):
        if value != self.initial_data.get('confirm_password', None):
            raise serializers.ValidationError(_(
                "The two password fields didn't match."
            ))

        password_validation.validate_password(value)

        return value

    def validate_city(self, value):
        if not value:
            raise serializers.ValidationError(_("This field is required."))

        return value


class UserUpdateSerializer(UserSerializer):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone_number' ,'city')


class UserPasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField()
    confirm_new_password = serializers.CharField()

    class Meta:
        fields = ('old_password', 'new_password', 'confirm_new_password')

    def validate_confirm_new_password(self, value):
        if value != self.initial_data['new_password']:
            raise serializers.ValidationError(_(
                "The two password fields didn't match."
            ))

        password_validation.validate_password(value)

        return value

    def validate_old_password(self, value):
        user = self.context['user']

        if not user.check_password(value):
            raise serializers.ValidationError(_(
                'Your old password was entered incorrectly. '
                'Please enter it again.'
            ))

        return value
