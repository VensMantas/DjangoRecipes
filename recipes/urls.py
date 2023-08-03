from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', views.RecipeListView.as_view(), name='recipes-home'),
    path('search/', views.RecipeSearchView.as_view(), name='recipes-search'),
    path('create/', views.RecipeCreateView.as_view(), name='recipes-create'),
    path('recipe/<int:pk>/', views.RecipeDetailView.as_view(), name="recipes-detail"),
    path('recipe/<int:pk>/update/', views.RecipeUpdateView.as_view(), name="recipes-update"),
    path('recipe/<int:pk>/delete/', views.RecipeDeleteView.as_view(), name="recipes-delete"),
    path('api-auth/', include('rest_framework.urls')),
    path('about/', views.about, name="recipes-about"),

    #JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    
    #API
    path('api/recipes/', views.RecipeListCreateView.as_view(), name='api-recipes-list-create'),
    path('api/recipes/<int:pk>/', views.RecipeRetrieveUpdateDestroyView.as_view(), name='api-recipes-retrieve-update-destroy'),
]

