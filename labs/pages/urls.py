from django.urls import path
# from this folder import views.py
from . import views

urlpatterns = [
    # the path will not work if not listed in pagess/views.py
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # path('contact', views.contact , name='contact'),
]