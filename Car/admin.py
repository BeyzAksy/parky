from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator

from .models import Car
from Users.models import User
from Core.utils import GROUP_DEFAULT

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    actions = ['delete_selected']

    fieldsets = (
        (_(u'Car Information'), {
            'fields' : ('plate', 'color', 'type'),
        }),
    )

    list_display = ('plate', 'type')
    list_filter = ('plate',)
    search_fields = ('plate', 'color', 'type')

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

    def get_queryset(self, request):
        qs = super(CarAdmin, self).get_queryset(request)

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
