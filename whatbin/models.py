from django.db import models


class Bin(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Item(models.Model):
    title = models.CharField(max_length=20)
    bin = models.ForeignKey(Bin)

    def __str__(self):  # __unicode__ on Python 2
        return self.title

