# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from django.urls import reverse


# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Registration(models.Model):
    APPROVE_CHOICES = (
        ('', 'Choose...'),
        ('Under-Process', 'Under-Process'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )
    BUSINESS_TYPES = (
    ('', 'Choose...'),
    ('Vehicle Loan', 'Vehicle Loan'),
    ('House Loan', 'House Loan'),
    ('Agriculture Loan', 'Agriculture Loan')
    )
    GENDER_CHOICES = (
        ('', 'Choose...'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other','Other'),
    )


    name=models.CharField(max_length=80)
    age=models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_posted = models.DateTimeField(default=timezone.now)
    address=models.TextField(default='')
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    zip=models.age=models.IntegerField(null=True)
    amount_required = models.IntegerField(null=True,blank=True)
    business_type = models.CharField(max_length=20, choices=BUSINESS_TYPES,null=True,blank=True)
    phone = models.CharField(max_length=32,null=True,blank=True)
    Approve_Reject=models.CharField(max_length=20, choices=APPROVE_CHOICES,null=True,blank=True,default='Under-Process')


    def __str__(self):
        return self.name





    def get_absolute_url(self):
        return reverse('person_changelist')
