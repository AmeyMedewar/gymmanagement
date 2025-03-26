from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Default home view for the app
    path('members/', views.member_list, name='member_list'),
    path('members/add/', views.member_create, name='member_create'),
    path('members/edit/<int:pk>/', views.member_update, name='member_update'),
    path('members/delete/<int:pk>/', views.member_delete, name='member_delete'),
]
