from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator

from Users.models import User
from Car.models import Car
from Park.models import Park
from .models import Rezervation
from Core.utils import GROUP_DEFAULT

@admin.register(Rezervation)
class RezervationAdmin(admin.ModelAdmin):
    actions = ['delete_selected']

    fieldsets = (
        (_(u'Personal Informations'), {
            'fields' : ('car', ),
        }),

        (_(u'Park Informations'), {
            'fields' : ('park','start_time','end_time')
        }),
    )

    list_display = ('park', 'start_time', 'end_time')

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "car" and not request.user.is_superuser:
            kwargs["queryset"] = Car.objects.filter(user=request.user)

        return super(RezervationAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = super(RezervationAdmin, self).get_queryset(request)

        if not request.user.is_superuser:
            qs = qs.filter(user=request.user.id)

        return qs

    def has_add_permission(self, request):
        group_names = [group.name for group in request.user.groups.all()]

        if request.user.is_superuser or GROUP_DEFAULT in group_names:
            return True
        else:
            return False

    def has_delete_permission(self, request, obj=None):
        group_names = [group.name for group in request.user.groups.all()]

        if request.user.is_superuser or GROUP_DEFAULT in group_names:
            return True
        else:
            return False
