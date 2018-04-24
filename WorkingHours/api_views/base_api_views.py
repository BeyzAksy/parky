# Third-Party
from rest_framework import viewsets, mixins

# Local Django
from WorkingHours.models import WorkingHours
from WorkingHours.serializers import (
    WorkingHoursSerializer, WorkingHoursListSerializer, WorkingHoursCreateSerializer,
    WorkingHoursRetrieveSerializer, WorkingHoursUpdateSerializer
)


class WorkingHoursViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      viewsets.GenericViewSet):
    queryset = WorkingHours.objects.all()

    def get_queryset(self):
        return self.queryset.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return WorkingHoursListSerializer
        elif self.action == 'create':
            return WorkingHoursCreateSerializer
        elif self.action == 'retrieve':
            return WorkingHoursRetrieveSerializer
        elif self.action == 'update':
            return WorkingHoursUpdateSerializer
        else:
            return WorkingHoursSerializer

    def get_permissions(self):
        permissions = super(WorkingHoursViewSet, self).get_permissions()

        if self.action in ['list', 'retrieve']:
            return []

        return permissions

    def perform_create(self, serializer):
        WorkingHours = serializer.save(user=self.request.user)
