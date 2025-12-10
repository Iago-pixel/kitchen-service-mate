from django.db import models
from django.contrib.auth.models import AbstractUser

from app import settings

class DishType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ("name", )

    def __str__(self):
        return self.name


class Cook(AbstractUser):
    years_of_experience = models.PositiveIntegerField()

    class Meta:
        ordering = ("username", )


class Ingredient(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ("name", )

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE, related_name="dishes")
    cooks = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="dishes")
    ingredients = models.ManyToManyField(Ingredient, related_name="dishes")

    class Meta:
        ordering = ("name", )

    def __str__(self):
        return f"{self.name} (price: {self.price}, type: {self.dish_type.name})"
