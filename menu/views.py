from django.shortcuts import render
from django.views import generic

from .models import Dish, Cook, DishType, Ingredient

def index(request):
    num_dishes = Dish.objects.count()
    num_cooks = Cook.objects.count()
    num_types_of_dishes = DishType.objects.count()
    num_ingredients = Ingredient.objects.count()
    context = {
        "num_dishes": num_dishes,
        "num_cooks": num_cooks,
        "num_types_of_dishes": num_types_of_dishes,
        "num_ingredients": num_ingredients,
    }
    return render(request, "menu/index.html", context=context)


class DishTypeListView(generic.ListView):
    model = DishType
    paginate_by = 10


class IngredientListView(generic.ListView):
    model = Ingredient
    paginate_by = 10


class DishListView(generic.ListView):
    model = Dish
    queryset = Dish.objects.select_related("dish_type")
    paginate_by = 10


class DishDetailView(generic.DetailView):
    model = Dish
