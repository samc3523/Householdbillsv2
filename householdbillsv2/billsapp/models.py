from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse

class Bill(models.Model):
    provider = models.CharField(max_length=255)
    btype = models.CharField(max_length=255)
    amount = models.FloatField()
    ogbody = models.TextField()
    date = models.CharField(max_length=255)
    fullpaid = models.BooleanField()
    santipaid = models.BooleanField()
    johnpaid = models.BooleanField()
    liampaid = models.BooleanField()
    sampaid = models.BooleanField()



