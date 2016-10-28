from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Read(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    data = models.CharField(max_length=4000)
    created_date = models.DateField()
    # country = models.CharField(max_length=50)
    # website = models.URLField()


class Write(models.Model):
    title = models.CharField(max_length=200)
    # url = models.URLField()
    data = models.CharField(max_length=4000)
    created_date = models.DateField()


class ReadWrite(models.Model):
    read = models.ForeignKey(Read)
    write = models.ForeignKey(Write)
