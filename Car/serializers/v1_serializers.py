# Local Django
from .base_serializers import (
    CarSerializer, CarListSerializer, CarCreateSerializer,
    CarRetrieveSerializer, CarUpdateSerializer,
)


class CarSerializerV1(CarSerializer):
    pass


class CarListSerializerV1(CarListSerializer):
    pass


class CarRetrieveSerializerV1(CarRetrieveSerializer):
    pass


class CarCreateSerializerV1(CarCreateSerializer):
    pass


class CarUpdateSerializerV1(CarUpdateSerializer):
    pass
