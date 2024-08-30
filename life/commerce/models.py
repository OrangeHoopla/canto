from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Item(models.Model):
    price = models.PositiveIntegerField
    name = models.CharField
    count = models.PositiveIntegerField

    options = (('Available','Available'),('Discontinued','Discontinued'),('Sold Out','Sold Out'))
    status = models.CharField(choices=options,default='Available',max_length=20)

    # class ItemObjects(models.Manager):
    #     def get_queryset(self) -> models.QuerySet:
    #         return super().get_queryset(),filter(status='Available')
    
    # class Meta:
    #     ordering = (' -price',)
    # objects = models.Manager() # default
    # itemobjects = ItemObjects() # custom

    def __str__(self):
        return "bob"