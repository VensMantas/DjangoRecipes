from django.test import TestCase
from django.contrib.auth.models import User
from .models import Recipe

class RecipeModelTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create two test recipes associated with the test user
        self.recipe1 = Recipe.objects.create(
            title='Test Recipe 1',
            description='Test description 1',
            ingredients='Test ingredients 1',
            instructions='Test instructions 1',
            cooking_time=30,
            author=self.user,
        )

        self.recipe2 = Recipe.objects.create(
            title='Test Recipe 2',
            description='Test description 2',
            ingredients='Test ingredients 2',
            instructions='Test instructions 2',
            cooking_time=45,
            author=self.user,
        )

    def test_recipe_creation(self):
        recipe = Recipe.objects.create(
            title='Test Recipe 3',
            description='Test description 3',
            ingredients='Test ingredients 3',
            instructions='Test instructions 3',
            cooking_time=20,
            author=self.user,
        )
        self.assertEqual(recipe.title, 'Test Recipe 3')
        self.assertEqual(recipe.cooking_time, 20)
        self.assertEqual(recipe.author, self.user)

    def test_recipe_update(self):
        self.recipe1.title = 'Updated Recipe Title'
        self.recipe1.save()
        updated_recipe = Recipe.objects.get(id=self.recipe1.id)
        self.assertEqual(updated_recipe.title, 'Updated Recipe Title')

    def test_recipe_deletion(self):
        recipe_count_before = Recipe.objects.count()
        self.recipe1.delete()
        recipe_count_after = Recipe.objects.count()
        self.assertEqual(recipe_count_before - 1, recipe_count_after)

    def test_recipe_listing(self):
        recipes = Recipe.objects.all()
        self.assertEqual(recipes.count(), 2)
        self.assertIn(self.recipe1, recipes)
        self.assertIn(self.recipe2, recipes)
