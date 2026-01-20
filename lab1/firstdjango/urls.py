# django app folder urls
# firstdjango/urls.py NOT myproject/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),    # homepage ofr 0.0.0.0:0000
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path("profile/<int:id>/", views.profile, name="profile"), # profile/1), profile/2
]
