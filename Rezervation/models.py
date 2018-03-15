from django.db import models
import os
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator

from Users.models import User
from Car.models import Car
from Park.models import Park

class Rezervation(models.Model):

    start_time = models.DateTimeField(verbose_name=_('Start Time'))
    end_time = models.DateTimeField(verbose_name=_('End Time'))
    user = models.ForeignKey(verbose_name=_('User') ,to=User)
    park = models.ForeignKey(verbose_name=_('Park') ,to=Park)
    car = models.ForeignKey(verbose_name=_('Car') ,to=Car)

    class Meta:
        verbose_name=_(u'Rezervation')
        verbose_name_plural=_(u'Rezervations')
