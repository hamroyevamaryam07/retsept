
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),

    # Shaxsiy admin panel
    path('my-admin/', views.custom_admin_dashboard, name='custom_admin_dashboard'),
    path('my-admin/add/', views.recipe_create, name='recipe_create'),
    path('my-admin/edit/<int:pk>/', views.recipe_update, name='recipe_update'),
    path('my-admin/delete/<int:pk>/', views.recipe_delete, name='recipe_delete'),
]
