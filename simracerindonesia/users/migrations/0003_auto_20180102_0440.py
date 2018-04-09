# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-02 04:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('users', '0002_auto_20180102_0409'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='simulator',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='favourite_cars',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='hardware',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='racing_simulator',
            field=models.ManyToManyField(blank=True, to='core.RacingSimulator'),
        ),
    ]