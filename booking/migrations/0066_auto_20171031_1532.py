# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-31 14:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0065_concert_tech_meat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concert',
            name='tech_meat',
            field=models.ManyToManyField(blank=True, related_name='tech_meat', to=settings.AUTH_USER_MODEL),
        ),
    ]
