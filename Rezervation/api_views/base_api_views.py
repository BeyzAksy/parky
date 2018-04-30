# Third-Party
from rest_framework import viewsets, mixins

# Local Django
from Rezervation.models import Rezervation
from Rezervation.serializers import (
    RezervationSerializer, RezervationListSerializer, RezervationCreateSerializer,
    RezervationRetrieveSerializer, RezervationUpdateSerializer
)


class RezervationViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      viewsets.GenericViewSet):
    queryset = Rezervation.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return RezervationListSerializer
        elif self.action == 'create':
            return RezervationCreateSerializer
        elif self.action == 'retrieve':
            return RezervationRetrieveSerializer
        elif self.action == 'update':
            return RezervationUpdateSerializer
        else:
            return RezervationSerializer

    def get_permissions(self):
        permissions = super(RezervationViewSet, self).get_permissions()

        if self.action in ['list', 'retrieve']:     #Böyle mi olmalı???
            return []

        return permissions

    def perform_create(self, serializer):
        Rezervation = serializer.save(user=self.request.user)
