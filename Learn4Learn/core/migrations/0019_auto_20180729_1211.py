# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-29 15:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20180729_1206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='course',
        ),
        migrations.AddField(
            model_name='skill',
            name='course',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Course'),
            preserve_default=False,
        ),
    ]
