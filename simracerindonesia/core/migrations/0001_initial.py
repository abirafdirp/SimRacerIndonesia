# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-25 04:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import simracerindonesia.core.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarManufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(blank=True, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(blank=True, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=100)),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='models', to='core.CarManufacturer')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RaceCar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(blank=True, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to=simracerindonesia.core.models.generate_race_car_picture_path)),
                ('name', models.CharField(help_text='With the mod name', max_length=50)),
                ('car_model', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.CarModel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RaceWeekend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(blank=True, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('date', models.DateField()),
                ('practice_start', models.TimeField()),
                ('qualify_start', models.TimeField()),
                ('race_start', models.TimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(blank=True, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
