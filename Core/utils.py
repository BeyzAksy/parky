# Django
from django.db.models import Q
from django.contrib.auth.models import Permission, Group

# Local Django
from Core.variables import GROUP_DEFAULT, GROUP_PARK


def create_group(group_name, permissions):
    try:
        group = Group.objects.get(name=group_name)

        group.permissions.clear()
        group.permissions.add(*permissions)
    except Group.DoesNotExist:
        group = Group.objects.create(name=group_name)
        group.permissions.add(*permissions)


def default():
    user_permissions = [
        p for p in Permission.objects.filter(
            Q(content_type__app_label__in=['Users'])
            & Q(codename__icontains='User')
        )
    ]
    car_permissions = [
        p for p in Permission.objects.filter(
            Q(content_type__app_label__in=['Car'])
        )
    ]

    rezervation_permissions = [
        p for p in Permission.objects.filter(
            Q(content_type__app_label__in=['Rezervation'])
        )
    ]

    create_group(GROUP_DEFAULT, (user_permissions + car_permissions + rezervation_permissions))

def park():
    user_permissions = [
        p for p in Permission.objects.filter(
            Q(content_type__app_label__in=['Users'])
            & Q(codename__icontains='User')
        )
    ]
    park_permissions = [
        p for p in Permission.objects.filter(
            Q(content_type__app_label__in=['Park'])
        )
    ]
    create_group(GROUP_PARK, (user_permissions + park_permissions))
