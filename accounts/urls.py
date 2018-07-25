from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views


app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.login, name = 'login'),
    path('logout/', auth_views.logout, {'next_page':'accounts:login'}, name = 'logout'),
]