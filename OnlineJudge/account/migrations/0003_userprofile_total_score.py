# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-08-20 02:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20170209_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='total_score',
            field=models.BigIntegerField(default=0),
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='accepted_problem_number',
            new_name='accepted_number',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='time_zone',
        )
    ]
