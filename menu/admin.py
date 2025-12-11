from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Dish, DishType, Ingredient, Cook


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "dish_type")
    list_filter = ("dish_type", )
    search_fields = ("name", )

admin.site.register(Cook, UserAdmin)
admin.site.register(DishType)
admin.site.register(Ingredient)
