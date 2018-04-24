# Third-Party
from rest_framework import viewsets, mixins

# Local Django
from Car.models import Car
from Car.serializers import (
    CarSerializer, CarListSerializer, CarCreateSerializer,
    CarRetrieveSerializer, CarUpdateSerializer
)


class CarViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      viewsets.GenericViewSet):
    queryset = Car.objects.all()

    def get_queryset(self):
        return self.queryset.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return CarListSerializer
        elif self.action == 'create':
            return CarCreateSerializer
        elif self.action == 'retrieve':
            return CarRetrieveSerializer
        elif self.action == 'update':
            return CarUpdateSerializer
        else:
            return CarSerializer

    def get_permissions(self):
        permissions = super(CarViewSet, self).get_permissions()

        if self.action in ['list', 'retrieve']:
            return []

        return permissions

    def perform_create(self, serializer):
        Car = serializer.save(user=self.request.user)
