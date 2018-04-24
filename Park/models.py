from django.db import models
import os
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator

from geoposition.fields import GeopositionField

from Users.models import User
from Core.models import City

class Park(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=50)
    capacity = models.PositiveSmallIntegerField(verbose_name=_('Capacity'))
    address = models.TextField(verbose_name=_('Address'))
    number_of_car_inside = models.PositiveSmallIntegerField(verbose_name=_('Number of Car'), blank=True)
    user = models.ForeignKey(verbose_name=_('User'),to=User)
    create_time= models.DateTimeField(verbose_name=_('Create Time'), auto_now_add=True)
    coordinate = GeopositionField(verbose_name=_('Coordinate'))
    city = models.ForeignKey(verbose_name=_('City'), to=City)


    class Meta:
        verbose_name=_(u'Park')
        verbose_name_plural=_(u'Parks')

    def __str__(self):
        return self.name
