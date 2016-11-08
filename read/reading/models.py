from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Tags(models.Model):
    tag = models.CharField(max_length=100)


class Write(models.Model):
    title = models.CharField(max_length=200)
    # url = models.URLField()
    data = models.CharField(max_length=4000)
    created_date = models.DateField()
    tags = models.ManyToManyField(Tags)


class Read(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    data = models.CharField(max_length=4000)
    created_date = models.DateField()
    tags = models.ManyToManyField(Tags)
    write = models.ForeignKey(Write, on_delete=models.SET_NULL, blank=True,
                              null=True, )
    # country = models.CharField(max_length=50)
    # website = models.URLField()

# class ReadWrite(models.Model):
#     read = models.ForeignKey(Read)
#     write = models.ForeignKey(Write)
