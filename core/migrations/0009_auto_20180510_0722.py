# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-10 01:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20180510_0626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]
