# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 08:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_remove_festival_concert'),
    ]

    operations = [
        migrations.AddField(
            model_name='festival',
            name='concerts',
            field=models.ManyToManyField(to='booking.Concert', verbose_name='list of concerts'),
        ),
    ]
