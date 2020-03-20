from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base-view'),
    path('register/', views.register, name='base-register'),
    path('login/', views.base, name='base-login'),
    path('logout/', views.base, name='base-logout'),
    path('profile/', views.base, name='base-profile'),
]
