# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-30 19:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20180701_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='username',
            field=models.CharField(default='spark934', max_length=15),
        ),
    ]
