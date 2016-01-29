# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-29 11:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ships', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ship',
            name='cargo_capacity_kg',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='ship',
            name='cost_in_credits',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='ship',
            name='docking_station_latitide',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='ship',
            name='docking_station_longitude',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='ship',
            name='hyperdrive_rating',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='ship',
            name='length',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='ship',
            name='manufacturer',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='ship',
            name='max_atmosphering_speed',
            field=models.BigIntegerField(null=True),
        ),
    ]