# Local Django
from .base_serializers import (
    RezervationSerializer, RezervationListSerializer, RezervationCreateSerializer,
    RezervationRetrieveSerializer, RezervationUpdateSerializer,
)


class RezervationSerializerV1(RezervationSerializer):
    pass


class RezervationListSerializerV1(RezervationListSerializer):
    pass


class RezervationRetrieveSerializerV1(RezervationRetrieveSerializer):
    pass


class RezervationCreateSerializerV1(RezervationCreateSerializer):
    pass


class RezervationUpdateSerializerV1(RezervationUpdateSerializer):
    pass
