# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-15 21:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0010_remove_mentorteam_candidates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='candidate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities', to=settings.AUTH_USER_MODEL),
        ),
    ]