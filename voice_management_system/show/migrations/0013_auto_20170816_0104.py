# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 01:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0012_auto_20170815_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentorscore',
            name='activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scores', to='show.Activity'),
        ),
    ]
