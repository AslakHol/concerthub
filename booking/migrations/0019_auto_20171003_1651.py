# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 14:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0018_remove_bookingoffer_artist_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingoffer',
            name='booker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]