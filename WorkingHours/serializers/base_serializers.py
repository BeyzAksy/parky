# Third-Party
from rest_framework import serializers

# Django
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

# Local Django
from Users.models import User
from WorkingHours.models import WorkingHours
from Park.models import Park
from Park.serializers import ParkSerializer

class WorkingHoursSerializer(serializers.ModelSerializer):
    park = ParkSerializer()
    type = serializers.CharField(source="get_type_display")
    start_time = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    end_time = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    class Meta:
        model = WorkingHours
        fields = ('id', 'park', 'type', 'start_time', 'end_time')


class WorkingHoursListSerializer(WorkingHoursSerializer):

    class Meta:
        model = WorkingHours
        fields = ('id', 'park', 'start_time', 'end_time')


class WorkingHoursRetrieveSerializer(WorkingHoursSerializer):
    pass


class WorkingHoursCreateSerializer(WorkingHoursSerializer):

    class Meta:
        model = WorkingHours
        fields = ('start_time','end_time')


class WorkingHoursUpdateSerializer(WorkingHoursSerializer):

    class Meta:
        model = WorkingHours
        fields = ('start_time', 'end_time')
