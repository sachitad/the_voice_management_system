# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-15 12:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0010_remove_mentorteam_candidates'),
        ('users', '0002_auto_20170812_0744'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='members', to='show.MentorTeam'),
            preserve_default=False,
        ),
    ]