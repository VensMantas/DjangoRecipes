from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class UserProfileTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.profile_url = reverse('user-profile')
        self.create_url = reverse('recipes-create')

    def test_user_profile_view(self):
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'/login/?next={self.profile_url}')

    def test_user_create_view(self):
        response = self.client.get(self.create_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'/login/?next={self.create_url}')

    def test_user_profile_view_with_recipes(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/profile.html')

    def test_user_create_recipe_page(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.create_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/recipe_form.html')
