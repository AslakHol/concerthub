# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 14:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0017_auto_20171003_1600'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookingoffer',
            name='artist_manager',
        ),
    ]
