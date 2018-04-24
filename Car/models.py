from django.db import models
import os
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator

from Users.models import User

class Car(models.Model):

        TYPE_CHOICES = (
            ('long', _('Long Car')),
            ('short', _('Short Car')),
        )

        plate = models.CharField(verbose_name=_('Plate'), max_length=50)
        color = models.CharField(verbose_name=_('Color'), max_length=50)
        type = models.CharField(verbose_name=_('Model'), max_length=50, choices=TYPE_CHOICES, default="short")
        user = models.ForeignKey(verbose_name=_('User'), to = User)

        class Meta:
            verbose_name=_(u'Car')
            verbose_name_plural=_(u'Cars')

        def __str__(self):
            return self.plate
