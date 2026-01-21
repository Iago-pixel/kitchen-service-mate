from django.test import TestCase

from menu.forms import CookCreationForm


class FormTests(TestCase):
    def test_cook_creation_form_valid_data(self):
        form_data = {
            "username": "testcook",
            "password1": "strongpassword123",
            "password2": "strongpassword123",
            "first_name": "Test",
            "last_name": "Cook",
            "years_of_experience": 5,
        }
        form = CookCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["username"], form_data["username"])
        self.assertEqual(form.cleaned_data["first_name"], form_data["first_name"])
        self.assertEqual(form.cleaned_data["last_name"], form_data["last_name"])
        self.assertEqual(form.cleaned_data["years_of_experience"], form_data["years_of_experience"])