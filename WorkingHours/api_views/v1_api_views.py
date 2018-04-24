# Local Django
from .base_api_views import WorkingHoursViewSet
from WorkingHours.serializers import (
    WorkingHoursSerializer, WorkingHoursListSerializerV1, WorkingHoursCreateSerializerV1,
    WorkingHoursRetrieveSerializerV1, WorkingHoursUpdateSerializerV1
)


class WorkingHoursViewSetV1(WorkingHoursViewSet):

    def get_serializer_class(self):
        if self.action == 'list':
            return WorkingHoursListSerializerV1
        elif self.action == 'create':
            return WorkingHoursCreateSerializerV1
        elif self.action == 'retrieve':
            return WorkingHoursRetrieveSerializerV1
        elif self.action == 'update':
            return WorkingHoursUpdateSerializerV1
        else:
            return WorkingHoursSerializerV1
