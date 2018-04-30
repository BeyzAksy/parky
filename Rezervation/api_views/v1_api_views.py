# Local Django
from .base_api_views import RezervationViewSet
from Rezervation.serializers import (
    RezervationSerializer, RezervationListSerializerV1, RezervationCreateSerializerV1,
    RezervationRetrieveSerializerV1, RezervationUpdateSerializerV1
)


class RezervationViewSetV1(RezervationViewSet):

    def get_serializer_class(self):
        if self.action == 'list':
            return RezervationListSerializerV1
        elif self.action == 'create':
            return RezervationCreateSerializerV1
        elif self.action == 'retrieve':
            return RezervationRetrieveSerializerV1
        elif self.action == 'update':
            return RezervationUpdateSerializerV1
        else:
            return RezervationSerializer
