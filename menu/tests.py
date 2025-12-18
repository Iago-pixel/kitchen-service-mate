from django.test import TestCase
from django.contrib.auth import get_user_model

from menu.models import DishType, Ingredient, Dish

class ModelsTests(TestCase):
    def test_dish_type_str(self):
        dish_type = DishType.objects.create(name="Appetizer")
        self.assertEqual(str(dish_type), "Appetizer")

    def test_ingredient_str(self):
        ingredient = Ingredient.objects.create(name="Tomato")
        self.assertEqual(str(ingredient), "Tomato")

    def test_cook_str(self):
        cook = get_user_model().objects.create(
            username="chef123",
            password="securepassword",
            first_name="Gordon",
            last_name="Ramsay"
        )
        self.assertEqual(str(cook), "chef123 - Gordon Ramsay")

    def test_dish_str(self):
        dish_type = DishType.objects.create(name="Main Course")
        dish = Dish.objects.create(
            name="Spaghetti Bolognese",
            description="Classic Italian pasta dish with meat sauce.",
            price=12.50,
            dish_type=dish_type
        )
        self.assertEqual(str(dish), "Spaghetti Bolognese (price: 12.50, type: Main Course)")

    def test_create_cook_with_experience(self):
        username = "chef456"
        password = "anotherpassword"
        first_name = "Jamie"
        last_name = "Oliver"
        years_of_experience = 10
        cook = get_user_model().objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            years_of_experience=years_of_experience
        )
        self.assertEqual(cook.years_of_experience, years_of_experience)
        self.assertEqual(cook.username, username)
        self.assertEqual(cook.first_name, first_name)
        self.assertEqual(cook.last_name, last_name)
        self.assertTrue(cook.check_password(password))
