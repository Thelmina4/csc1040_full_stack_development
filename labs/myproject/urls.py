"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# see below, both 'path' and 'include' are used in urlpatterns

urlpatterns = [
    # visiting /admin/ will show Django's built-in admin interface.
    path('admin/', admin.site.urls),
    # my additional paths
    # tell the urlpatterns to include pages/urls.py/urlpatterns as allowed views

    # / and /about/ are handled by the pages app
    # /products/ and /products/123/ are handled by the products app
    # /cart/ and /cart/checkout/ are handled by the cart app
    path('', include('pages.urls')),                # pages at root
    path('products/', include('products.urls')),    # products at /products/
    path('cart/', include('cart.urls')),            # cart at /cart/
]
