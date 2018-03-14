from django.db import models

from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from geoposition.fields import GeopositionField

class City(models.Model):
    city = models.CharField(verbose_name=_('City'), max_length=55, unique=True)

    class Meta:
        verbose_name=_(u'City')
        verbose_name_plural=_(u'Cities')

    def __str__(self):
        return self.city
