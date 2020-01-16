# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-15 06:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('POC', '0011_registration_date_posted'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='amount_required',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='business_type',
            field=models.CharField(choices=[('', 'Choose...'), ('Vehicle Loan', 'Vehicle Loan'), ('House Loan', 'House Loan'), ('Agriculture Loan', 'Agriculture Loan')], max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='phone',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='gender',
            field=models.CharField(choices=[('', 'Choose...'), ('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10),
        ),
    ]