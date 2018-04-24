# Local Django
from .base_api_views import CityViewSet
from Core.serializers import (
    CitySerializer, CitySerializerV1
)
from Core.models import City


class CityViewSetV1(CityViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
