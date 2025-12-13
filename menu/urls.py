from django.urls import path

from .views import (
    index,
    DishTypeListView,
    IngredientListView,
    DishListView,
    DishDetailView,
    CookListView,
    CookDetailView,
    DishTypeCreateView,
    IngredientCreateView,
)

urlpatterns = [
    path("", index, name="index"),
    path("dish-types/", DishTypeListView.as_view(), name="dish-type-list"),
    path("dish-types/create/", DishTypeCreateView.as_view(), name="dish-type-create"),
    path("ingredients/", IngredientListView.as_view(), name="ingredient-list"),
    path(
        "ingredients/create", IngredientCreateView.as_view(), name="ingredient-create"
    ),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/<int:pk>", DishDetailView.as_view(), name="dish-detail"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("cooks/<int:pk>", CookDetailView.as_view(), name="cook-detail"),
]

app_name = "menu"
