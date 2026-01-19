# django app folder urls
# firstdjango/urls.py NOT myproject/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('contact/', views.contact, name="contact")
]
