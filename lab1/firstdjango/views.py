from math import log
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Book, Author
from .forms import *

# Create your views here.
def home(request):
    username = request.GET.get('username', 'DEFAULT')
    return render(request, 'home.html', {'username':username})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

# /profile/1 -> alice
# /profile/2 -> bob
def profile(request, id):
    users = {
        1: {"username": "Alice", "age":30},
        2: {"username": "bob", "age":25},
        3: {"username": "mary", "age":52}
    }

    user = users.get(id) # None if not found
    if user is None:
        # a user was not found
        return render(request, "not_found.html", {'error':f"user w id {id} not found"} )
    else:
        return render(request, "profile.html", {"user":users[id]})

# week 2 notes
def books(request):
    all_books = Book.objects.all()
    # need to know what datatype we are rendering
    # list of book objects.
    # all_books = Book.objects.all() returns an array of books
    return render(request, 'all_books.html', {'books': all_books})

def book_detail(request, id):
    # book = Book.objects.get(id=id) # returns a single book object
    # Book -> models.py class Book
    book = get_object_or_404(Book, id=id) # this is better than the line above
    # returns a single book object
    return render(request, 'book_detail.html', {'book': book})

def author_detail(request, id):
    author = get_object_or_404(Author, id=id) # returns a single author object
    return render(request, 'author_detail.html', {'author': author})

# def is_staff(user):
#     return user.is_staff()

@login_required
@user_passes_test(lambda u: u.is_staff)
def add_author(request):
    # django can do the next 2 lines for us
    # user = request.user
    # user.is_authenticated # True or False

    if request.method=="POST":
        # IMPORTANT!!!!
        # WE NEED TO ADD THIS TO VALIDATE THE DATA
        # User  has pressed "Submit" and is uploading data we need to save
        authorform = Authorform(request.POST)
        if authorform.is_valid():
            authorform.save() #save the new author to the daatabase
            return render(request, 'author_added.html', {'author': authorform.instance})
    else:
        # visiter is vitsiting the page for the FIRST TIME , SHOW THEM THE EMPTY FOR
        authorform = Authorform()

    return render(request, 'author_added.html', {'form': authorform})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
