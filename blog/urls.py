"""iblogs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from .views import home, post,category
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('blog/<slug:url>/', views.post, name='post_detail'),
    path('category/<slug:url>/', views.category, name='category'),
    path('category/<slug:url>/', views.category_detail, name='category_detail'),
    path('category/<str:category_url>/add-post/', views.add_post, name='add_post'),
    path('about/', views.about_page, name='about'),
    path('update-post/<int:post_id>/', views.update_post, name='update_post'),
    path('delete-post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
