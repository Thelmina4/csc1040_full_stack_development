from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'pages/home.html', {
        'title': 'Home Page',
        'descrition': 'The home page for myproject'
    })

def about(request):
    return render(request, 'pages/about.html',  {
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
