from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class AdminSiteTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="testadmin"
        )
        self.client.force_login(self.admin_user)
        self.cook = get_user_model().objects.create_user(
            username="cook",
            password="testcook",
            years_of_experience=4,
        )

    def test_cook_years_of_experience_listed(self):
        """
        Test that cook's years of experience is in display an cook admin page
        """
        url = reverse("admin:menu_cook_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.cook.years_of_experience)

    def test_cook_years_of_experience_detail_listed(self):
        """
        Test that cook's years of experience is on cook detail admin page
        """
        url = reverse("admin:menu_cook_change", args=[self.cook.id])
        res = self.client.get(url)
        self.assertContains(res, self.cook.years_of_experience)
