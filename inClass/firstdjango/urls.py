# django app folder urls
# firstdjango/urls.py NOT myproject/urls.py

from django.urls import path
from . import views
from rest_framework.routers import 

router = DefaultRouter()
router.register()
# now runserver

# 127.0.0.1:8000/api/authors
# 127.0.0.1:8000/api/authors/1
# go to terminal and send a curl req 
# curl http://127.0.0.1:8000/api/authors/2/

# go to browser
# 127.0.0.1:8000/api/authors/?genre=Fiction

# go to incognito 
# 127.0.0.1:8000/api/authors/
# go to raw data



urlpatterns = [
    path('', views.home, name="home"),    # homepage ofr 0.0.0.0:0000
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    # if there is no profile for user then there is an else in views.py
    path("profile/<int:id>/", views.profile, name="profile"), # profile/1), profile/2
    
    # making a database for books and authors
    # the basic books page
    path("books/", views.books,  name='all_books'),
    # the page for a particular book
    # views.py -> def book_detail: what to do
    # name="author_detail" == the name of the html page
    path("book/<int:id>/", views.book_detail, name="book_detail"),
    
    path("authors/add/", views.add_author, name="add_author"),
    path("authors/<int:id>/", views.author_detail, name="author_detail"),
    
    path("register/", views.register, name="register"),
]
