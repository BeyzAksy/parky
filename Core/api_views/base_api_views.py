# Third-Party
from rest_framework import viewsets, mixins
from djoser.views import LoginView as _LoginView
# Local Django
from Users.models import User
from Core.models import City
from Core.serializers import (
    CitySerializer
)


class LoginView(_LoginView):

    def _action(self, serializer):
        action = super(LoginView, self)._action(serializer)

        action.data.update({
            'user_id': serializer.user.id,
        })

        return action


class CityViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def get_permissions(self):
        permissions = super(CityViewSet, self).get_permissions()

        if self.action in ['list']:
            return []

        return permissions
