# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-22 07:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('POC', '0007_auto_20191122_0529'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='phoneno',
            field=models.IntegerField(null=True),
        ),
    ]