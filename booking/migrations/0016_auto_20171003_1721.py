# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0015_bookingoffer_offering_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='festival',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='festival',
            name='start_time',
        ),
        migrations.RemoveField(
            model_name='festival',
            name='tickets',
        ),
        migrations.AddField(
            model_name='festival',
            name='num_of_concerts',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='festival',
            name='total_revenue',
            field=models.FloatField(blank=True, null=True),
        ),
    ]