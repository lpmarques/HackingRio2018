# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-29 02:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20180728_2349'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skill',
            old_name='skill',
            new_name='name',
        ),
    ]
