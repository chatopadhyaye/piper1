# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-09 09:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20180709_1449'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='usern',
            new_name='username',
        ),
    ]
