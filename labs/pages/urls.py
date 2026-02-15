from django.urls import path
# from this folder import views.py
from . import views

urlpatterns = [
    # the path will not work if not listed in pagess/views.py
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # path('contact', views.contact , name='contact'),

    # the next line is the line thaat we wants us to use. 
    path('users/<int:id>/', views.user_profile, name='user_profile'),
    # this line only works because I made a try execpt for it
    # path('users/<id>/', views.user_profile),
    # path('search/<category>/', views.search),
    path('books/', views.book_list, name='book_list'),
    path('books/search/', views.book_search, name='book_search'),
    path('books/add/', views.add_book, name='add_book'),

    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('authors/<int:author_id>/', views.author_detail, name='author_detail'),

    path('books/category/<str:cat_id>/', views.category, name='category'),
    path('books/category/<str:cat_id>/year/<int:year>/', views.books_by_cat_and_year, name='cat_year_filter'),

    # login & register
    path('register/', views.register, name='register'),

]