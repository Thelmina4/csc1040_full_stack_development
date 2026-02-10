from django.shortcuts import render

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
