# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-15 11:40
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0008_activity_date_of_performance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentorscore',
            name='score',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
    ]