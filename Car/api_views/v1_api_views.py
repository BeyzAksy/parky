# Local Django
from .base_api_views import CarViewSet
from Car.serializers import (
    CarSerializer, CarListSerializerV1, CarCreateSerializerV1,
    CarRetrieveSerializerV1, CarUpdateSerializerV1
)


class CarViewSetV1(CarViewSet):

    def get_serializer_class(self):
        if self.action == 'list':
            return CarListSerializerV1
        elif self.action == 'create':
            return CarCreateSerializerV1
        elif self.action == 'retrieve':
            return CarRetrieveSerializerV1
        elif self.action == 'update':
            return CarUpdateSerializerV1
        else:
            return CarSerializer
