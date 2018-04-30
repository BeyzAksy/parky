# Django
from django.conf.urls import url, include
from django.core.urlresolvers import reverse
# Third-Party
from rest_framework import routers

# Local Django
from Users.api_views import UserViewSetV1
from Core.api_views import CityViewSetV1
from Car.api_views import CarViewSetV1
from Park.api_views import ParkViewSetV1
from Rezervation.api_views import RezervationViewSetV1
from WorkingHours.api_views import WorkingHoursViewSetV1

router_V1 = routers.DefaultRouter()

LIST_V1 = [
    (r'users', UserViewSetV1, 'users'),
    (r'cars', CarViewSetV1, 'cars'),
    (r'cities', CityViewSetV1, 'cities'),
    (r'parks', ParkViewSetV1, 'parks'),
    (r'rezervations', RezervationViewSetV1, 'rezervations'),
    (r'workinghours', WorkingHoursViewSetV1, 'workinghours'),
]

for router in LIST_V1:
    router_V1.register(router[0], router[1], base_name=router[2])


urlpatterns = [
    url(r'v1/', include(router_V1.urls, namespace='v1')),
]
