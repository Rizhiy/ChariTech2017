# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 16:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slate2learn', '0002_auto_20170317_1439'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='learner',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='learner',
            name='name',
        ),
        migrations.RemoveField(
            model_name='learner',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='learner',
            name='time_slot',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='credit_balance',
        ),
    ]
