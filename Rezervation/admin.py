from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator

from Users.models import User
from Car.models import Car
from Park.models import Park
from .models import Rezervation

@admin.register(Rezervation)
class RezervationAdmin(admin.ModelAdmin):
    actions = ['delete_selected']

    fieldsets = (
        (_(u'Personal Informations'), {
            'fields' : ('user','car'),
        }),

        (_(u'Park Informations'), {
            'fields' : ('park','start_time','end_time')
        }),
    )
    list_display = ('user','park', 'start_time', 'end_time')
    search_fields = ('user',)
