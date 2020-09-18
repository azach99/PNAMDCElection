from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'Submission-home'),
    path('profile/', views.profile, name = 'profile'),
]