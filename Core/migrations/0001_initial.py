# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('city', models.CharField(verbose_name='City', max_length=55, unique=True)),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'Cities',
            },
        ),
    ]
