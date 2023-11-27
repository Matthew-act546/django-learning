"""
URL configuration for trydjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from courses.views import (
    CourseView, 
    my_fbv, 
    CourseListView, 
    CourseCreateView, 
    CourseUpdateView, 
    CourseDeleteView
)

app_name = 'courses'
urlpatterns = [
    path('', CourseListView.as_view(), name='course-list'),
    path('create/', CourseCreateView.as_view(), name='course-create'),
    path('<int:my_id>/', CourseView.as_view(), name='course-detail'),
    path('<int:my_id>/update/', CourseUpdateView.as_view(), name='course-update'),
    path('<int:my_id>/delete/', CourseDeleteView.as_view(), name='course-delete'),
    # path('', my_fbv, name='course-list')
    
]
