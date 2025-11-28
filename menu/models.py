from django.db import models
from django.contrib.auth.models import AbstractUser

from kitchen_service_mate import settings

class DishType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Cook(AbstractUser):
    experience_years = models.PositiveIntegerField()

    class Meta:
        ordering = ('username',)


class Dish(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    cooks = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='dishes')

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
