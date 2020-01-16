# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-15 06:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('POC', '0013_auto_20200115_0649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='amount_required',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='business_type',
            field=models.CharField(blank=True, choices=[('', 'Choose...'), ('Vehicle Loan', 'Vehicle Loan'), ('House Loan', 'House Loan'), ('Agriculture Loan', 'Agriculture Loan')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='phone',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
