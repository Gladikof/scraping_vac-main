from tabnanny import verbose
from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=77, 
                            verbose_name='City name', unique = True)

    slug = models.CharField(max_length=77, blank = True , unique = True)

    class Meta:
        verbose_name = 'City name'
        verbose_name_plural = 'Citys names'
        

    def __str__(self) -> str:
            return self.name


class Language(models.Model):
    name = models.CharField(max_length=77, 
                            verbose_name='Programming language', unique = True)

    slug = models.CharField(max_length=77, blank = True , unique = True)

    class Meta:
        verbose_name = 'Programming language'
        verbose_name_plural = 'Programming languages'

    def __str__(self) -> str:
            return self.name