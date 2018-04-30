# Local Django
from .base_api_views import ParkViewSet
from Park.serializers import (
    ParkSerializer, ParkListSerializerV1, ParkCreateSerializerV1,
    ParkRetrieveSerializerV1, ParkUpdateSerializerV1
)


class ParkViewSetV1(ParkViewSet):

    def get_serializer_class(self):
        if self.action == 'list':
            return ParkListSerializerV1
        elif self.action == 'create':
            return ParkCreateSerializerV1
        elif self.action == 'retrieve':
            return ParkRetrieveSerializerV1
        elif self.action == 'update':
            return ParkUpdateSerializerV1
        else:
            return ParkSerializer
