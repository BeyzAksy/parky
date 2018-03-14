from django.db import models
import os
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator

from Park.models import Park

class WorkingHours(models.Model):

    TYPE_CHOICES = (
        ('weekdays', _('Weekdays')),
        ('weekdays+saturday', _('Weekdays + Saturday')),
        ('weekdays+weekend', _('Weekdays + Weekend')),
    )

    start_time = models.DateTimeField(verbose_name=_('Start Time'))
    end_time = models.DateTimeField(verbose_name=_('End Time'))
    park = models.ForeignKey(verbose_name=_('Park') ,to=Park)
    type = models.CharField(verbose_name=_('Days'), max_length=50, choices=TYPE_CHOICES, default="weekdays")

    class Meta:
        verbose_name = _('WorkingHours')
        verbose_name_plural = _('WorkingHours')

    #def __str__(self):
    #    return self.name
