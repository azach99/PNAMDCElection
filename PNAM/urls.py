"""PNAM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from Users import views as Users_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Submission.urls')),
    path('register/', Users_views.register, name = 'register'),
    path('login/', auth_views.LoginView.as_view(template_name = 'Users/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'Users/logout.html'), name = 'logout'),
    path('submission/', Users_views.submission, name = 'submission'),
    path('list_subs/', include('Users.urls'), name = 'list'),
    path('results/', Users_views.results, name = 'results')
]
