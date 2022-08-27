from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=77)
    slug = models.CharField(max_length=77, blank = True)