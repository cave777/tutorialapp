"""newsapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from . import views

app_name = 'tutorial'

urlpatterns = [
    # path('series/<slug>', views.tutorial_series_detail, name = 'tutorial_series_detail'),
    path('series/<slug>', view=views.TutorialSeriesDetailView.as_view(), name='tutorial_series_detail'),
    # path('series/<tutorial_series>/<slug>', view = views.LessonDetailView.as_view(), name='lesson_detail'),
    path('series/<tutorial_series>/<slug>', view=views.lesson_detail, name='lesson_detail'),
    path('series/', views.tutorial_series_list, name='tutorial_series_list'),
]
