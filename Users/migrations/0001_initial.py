# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0001_initial'),
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True, null=True)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', default=False, help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('email', models.EmailField(verbose_name='Email', max_length=255, unique=True)),
                ('first_name', models.CharField(verbose_name='First Name', max_length=50)),
                ('last_name', models.CharField(verbose_name='Last Name', max_length=50)),
                ('is_active', models.BooleanField(verbose_name='Active', default=True)),
                ('city', models.ForeignKey(verbose_name='City', null=True, to='Core.City')),
                ('groups', models.ManyToManyField(verbose_name='groups', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group')),
                ('user_permissions', models.ManyToManyField(verbose_name='user permissions', blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
    ]
