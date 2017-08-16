# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-15 21:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20170815_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('C', 'Candidate'), ('M', 'Mentor'), ('A', 'Admin')], max_length=1, verbose_name='Type of User'),
        ),
    ]