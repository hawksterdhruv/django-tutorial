# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-04 12:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reading', '0002_auto_20161104_0453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='read',
            name='tags',
            field=models.ManyToManyField(null=True, to='reading.Tags'),
        ),
    ]
