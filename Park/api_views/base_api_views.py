# Third-Party
from rest_framework import viewsets, mixins

# Local Django
from Park.models import Park
from Park.serializers import (
    ParkSerializer, ParkListSerializer, ParkCreateSerializer,
    ParkRetrieveSerializer, ParkUpdateSerializer
)


class ParkViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      viewsets.GenericViewSet):
    queryset = Park.objects.all()

    def get_queryset(self):
        return self.queryset.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ParkListSerializer
        elif self.action == 'create':
            return ParkCreateSerializer
        elif self.action == 'retrieve':
            return ParkRetrieveSerializer
        elif self.action == 'update':
            return ParkUpdateSerializer
        else:
            return ParkSerializer

    def get_permissions(self):
        permissions = super(ParkViewSet, self).get_permissions()

        if self.action in ['list', 'retrieve']:     #Böyle mi olmalı???
            return []

        return permissions

    def perform_create(self, serializer):
        Park = serializer.save(user=self.request.user)
