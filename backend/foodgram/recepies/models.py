from django.db import models
from users.models import User


class Ingredient(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Название'
    )
    measurement_unit = models.CharField(
        max_length=200,
        verbose_name='Единицы измерения'
    )
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name} - {self.measurement_unit}'


class Tag(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name='Название'
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        verbose_name='Адрес'
    )
    color = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Цвет'
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'

