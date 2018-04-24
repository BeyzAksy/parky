# Local Django
from .base_serializers import (
    ParkSerializer, ParkListSerializer, ParkCreateSerializer,
    ParkRetrieveSerializer, ParkUpdateSerializer,
)


class ParkSerializerV1(ParkSerializer):
    pass


class ParkListSerializerV1(ParkListSerializer):
    pass


class ParkRetrieveSerializerV1(ParkRetrieveSerializer):
    pass


class ParkCreateSerializerV1(ParkCreateSerializer):
    pass


class ParkUpdateSerializerV1(ParkUpdateSerializer):
    pass
