from django.urls import path
from . import views

urlpatterns = [
    path('', views.monument_list, name='monument_list'),
    path('create/', views.monument_create, name='monument_create'),
    path('update/<int:pk>/', views.monument_update, name='monument_update'),
    path('delete/<int:pk>/', views.monument_delete, name='monument_delete'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
