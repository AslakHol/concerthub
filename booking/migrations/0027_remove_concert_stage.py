# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 15:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0026_auto_20171007_1719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='concert',
            name='stage',
        ),
    ]
