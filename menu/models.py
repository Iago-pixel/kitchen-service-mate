from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.core.validators import MaxValueValidator

from app import settings


class DishType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Cook(AbstractUser):
    years_of_experience = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(50)])

    class Meta:
        ordering = ("username",)

    def __str__(self):
        return f"{self.username} - {self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("menu:cook-detail", args=[str(self.id)])


class Ingredient(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    dish_type = models.ForeignKey(
        DishType, on_delete=models.CASCADE, related_name="dishes"
    )
    cooks = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="dishes")
    ingredients = models.ManyToManyField(Ingredient, related_name="dishes")

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return f"{self.name} (price: {'{:.2f}'.format(self.price)}, type: {self.dish_type.name})"

    def get_absolute_url(self):
        return reverse("menu:dish-detail", args=[str(self.id)])
