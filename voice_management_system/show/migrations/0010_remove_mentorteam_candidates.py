# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-15 12:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0009_auto_20170815_1140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentorteam',
            name='candidates',
        ),
    ]