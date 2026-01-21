from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from menu.models import DishType

DISH_TYPE_URL = reverse("menu:dish-type-list")

class PublicDishTypeTest(TestCase):
    def test_login_required(self):
        res = self.client.get(DISH_TYPE_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateDishTypeTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="testpass",
        )
        self.client.force_login(self.user)

    def test_retrieve_dish_types(self):
        DishType.objects.create(name="Appetizer")
        DishType.objects.create(name="Dessert")
        res = self.client.get(DISH_TYPE_URL)
        self.assertEqual(res.status_code, 200)
        dish_types = DishType.objects.all()
        self.assertEqual(len(res.context["dishtype_list"]), dish_types.count())
        self.assertTemplateUsed(res, "menu/dishtype_list.html")


class PrivateCookTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="cookuser",
            password="cookpass",
        )
        self.client.force_login(self.user)

    def test_create_cook(self):
        form_data = {
            "username": "newcook",
            "password1": "newstrongpassword123",
            "password2": "newstrongpassword123",
            "first_name": "New",
            "last_name": "Cook",
            "years_of_experience": 3,
        }
        self.client.post(reverse("menu:cook-create"), form_data)
        new_cook = get_user_model().objects.get(username=form_data["username"])

        self.assertEqual(new_cook.first_name, form_data["first_name"])
        self.assertEqual(new_cook.last_name, form_data["last_name"])
        self.assertEqual(new_cook.years_of_experience, form_data["years_of_experience"])
