from django.urls import path

from .views import index, DishTypeListView, IngredientListView, DishListView

urlpatterns = [
    path("", index, name="index"),
    path("dish-types/", DishTypeListView.as_view(), name="dish-type-list"),
    path("ingredients/", IngredientListView.as_view(), name="ingredient-list"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
]

app_name = "menu"
