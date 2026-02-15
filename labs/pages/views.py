from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import Book, Author
from .forms import BookForm

# Create your views here.
def home(request):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    username = request.GET.get('username', 'Guest')
    return render(request, 'home.html', {
        'numbers': numbers,
        'username': username,

        'title': 'Home Page',
        'description': 'The home page for myproject',
        'items': ['Django', 'Python', 'HTML'],
    })

# this about fucntion is linked to views.about in pages/urls.py
def about(request):
    return render(request, 'about.html',  {
        'title': 'About Us',
        'description': 'Learn more about our company.'
    })

def products(request):
    return render(request, 'pages/products.html',  {
        'title': 'Products',
        'description': 'List of products our company sells.'
    })

def cart(request):
    return render(request, 'pages/cart.html',  {
        'title': 'Cart',
        'description': 'Cart for the products you would like to buy.'
    })

def user_profile(request, id):
    # In a real app, you'd fetch this from a database
    users = {
        1: {'name': 'Alice', 'email': 'alice@email.com'},
        2: {'name': 'Bob', 'email': 'bob@email.com'},
        3: {'name': 'Mary', 'email': 'mary@email.com'},
    }
    # this won't work because I declare that it is an int in urls.py
    try:
        # convert to int and try to output the 
        user_id = int(id)
    except ValueError:
        return render(request, 'not_found.html', {'id': id})
    
    user = users.get(id)
    if user is None:
       return render(request, 'not_found.html', {'id': id})
    
    
    return render(request, 'profile.html', {'user': user, 'id': id})

# category = 'books' (from the URL path)
# query = 'python' (from GET parameters)
# page = '2' (from GET parameters)

def search(request, category):
    query = request.GET.get('q', '')
    page = request.GET.get('page', 1)

    return render(request, 'search.html', {
        'category': category,
        'query': query,
        'page': page
    })

def get_books(request):
    books = Book.object.filter(year_published__gt=1950)
    # books is a list of Book objects
    # Access fields by name: books[0].title
    # this needs a return render to work

def book_list(request):
    books = Book.objects.all()  # Get ALL books from the database
    return render(request, 'book_list.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_detail.html', {'book': book})

def book_search(request):
    query = request.GET.get('q', '')  # Get the 'q' parameter, default to empty string

    if query:
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.none()  # Return empty queryset if no search term

    return render(request, 'book_search.html', {'books': books, 'query': query})


def author_detail(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    books = Book.objects.filter(author=author)  # Get all books by this author
    return render(request, 'author_detail.html', {'author': author, 'books': books})

def category(request, cat_id):
    by_category = Book.objects.filter(category=cat_id)
    return render(request, 'book_list.html', {'books': by_category} )

def books_by_cat_and_year(request, cat_id, year):
    # Filter where category matches AND year_published matches
    filtered_books = Book.objects.filter(category=cat_id, year_published=year)
    
    context = {
        'books': filtered_books,
        'category_name': cat_id,
        'year': year
    }
    
    # Reusing existing list template (DRY Principle)
    return render(request, 'book_list.html', context)

@login_required
def add_book(request):
    # if I didn't put in @login_required
    # I would use the next 2 lines
    # if not request.user.is_authenticated:
    #     return redirect('login')
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.added_by = request.user
            form.save()
            return redirect('book_list') # Redirect to a GET page
    else:
        form = BookForm()

    return render(request, 'add_book.html', {'form': form})

# UserCreationForm same as add_book
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save
            return redirect('login')
        
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})
