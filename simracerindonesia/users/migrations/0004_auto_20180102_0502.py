# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-02 05:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20180102_0440'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='racing_simulator',
            new_name='racing_simulators',
        ),
    ]