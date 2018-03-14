from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
from django.contrib.auth.models import Group

from .models import Park
from Users.models import User
from Core.models import City
from Core.utils import GROUP_DEFAULT

@admin.register(Park)
class ParkAdmin(admin.ModelAdmin):
    actions = ['delete_selected']

    fieldsets = (
        (_(u'Park Information'), {
            'fields' : ('name', 'capacity','number_of_car_inside'),
        }),
        (_(u'Personal Informations'), {
            'fields' : ('users',),
        }),
        (_(u'Address Informations'), {
            'fields' : ('city', 'address', 'coordinate'),
        }),
    )

    list_display = ('name', 'capacity', 'number_of_car_inside', 'create_time')
    list_filter = ('name',)
    search_fields = ('name',)
