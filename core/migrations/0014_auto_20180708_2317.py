# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-08 17:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20180701_0122'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='username',
            new_name='usern',
        ),
    ]