# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-07 15:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0072_merge_20171105_1848'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artist',
            old_name='artist_rev',
            new_name='artist_review',
        ),
    ]
