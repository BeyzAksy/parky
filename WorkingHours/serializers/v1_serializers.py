# Local Django
from .base_serializers import (
    WorkingHoursSerializer, WorkingHoursListSerializer, WorkingHoursCreateSerializer,
    WorkingHoursRetrieveSerializer, WorkingHoursUpdateSerializer,
)


class WorkingHoursSerializerV1(WorkingHoursSerializer):
    pass


class WorkingHoursListSerializerV1(WorkingHoursListSerializer):
    pass


class WorkingHoursRetrieveSerializerV1(WorkingHoursRetrieveSerializer):
    pass


class WorkingHoursCreateSerializerV1(WorkingHoursCreateSerializer):
    pass


class WorkingHoursUpdateSerializerV1(WorkingHoursUpdateSerializer):
    pass
