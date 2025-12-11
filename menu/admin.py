from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Dish, DishType, Ingredient, Cook

admin.site.register(Cook, UserAdmin)
admin.site.register(DishType)
admin.site.register(Ingredient)
admin.site.register(Dish)
