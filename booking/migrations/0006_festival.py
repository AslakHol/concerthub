# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 07:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_auto_20170919_1843'),
    ]

    operations = [
        migrations.CreateModel(
            name='Festival',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('concert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.Concert')),
            ],
        ),
    ]
