from django.contrib import admin

from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
from .models import WorkingHours
from Park.models import Park

@admin.register(WorkingHours)
class WorkingHoursAdmin(admin.ModelAdmin):
    actions = ['delete_selected']

    fieldsets = (
        (_(u'Working Hours'), {
            'fields' : ('type','start_time', 'end_time'),
        }),
        (_(u'Park Informations'), {
            'fields' : ('park',),
        }),
    )

    list_display = ('park','type','start_time', 'end_time')
    search_fields = ('type',)
