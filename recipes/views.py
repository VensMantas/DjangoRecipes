from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.db.models import Q

from . import models

from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Recipe
from .serializers import RecipeSerializer
from .permissions import IsAuthorOrReadOnly

#REST API classes
class RecipeListCreateView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class RecipeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def update(self, request, *args, **kwargs):
        request.data['author'] = request.user.id
        return super().update(request, *args, **kwargs)

# WebAPP classes
def home(request):
    recipes = models.Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, "recipes/home.html", context)

#Listing recipes
class RecipeListView(ListView):
    model = models.Recipe
    template_name = 'recipes/home.html'
    context_object_name = 'recipes'
    ordering = '-created_at' 

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return models.Recipe.objects.filter(
                Q(title__icontains=query) |
                Q(ingredients__icontains=query) |
                Q(cooking_time__icontains=query)
            ).order_by(self.ordering)
        return super().get_queryset()

#Search recipes
class RecipeSearchView(ListView):
    model = models.Recipe
    template_name = 'recipes/search_results.html'
    context_object_name = 'recipes'
    ordering = '-created_at'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return models.Recipe.objects.filter(
                Q(title__icontains=query) |
                Q(ingredients__icontains=query) |
                Q(cooking_time__icontains=query)
            ).order_by(self.ordering)
        return super().get_queryset()

class RecipeDetailView(DetailView):
    model = models.Recipe

#Create recipe
class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = models.Recipe
    fields = ['title', 'description', 'ingredients', 'instructions', 'cooking_time', 'image']

    def form_valid (self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

#Update recipe
class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Recipe
    fields = ['title', 'description', 'ingredients', 'instructions', 'cooking_time', 'image']

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author

    def form_valid (self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

#Delete recipe    
class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Recipe
    success_url = reverse_lazy('recipes-home')

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author 

def about(request):
    return render(request, "recipes/about.html", {'title':'About us'})