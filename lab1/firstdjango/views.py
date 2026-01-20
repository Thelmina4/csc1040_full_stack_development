from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    username = request.GET.get('username', 'Default')
    return render(request, 'home.html', {'username':username})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

# /profile/1 -> alice
# /profile/2 -> bob
def profile(request, id):
    users = {
        1: {"username": "alice", "age":30},
        2: {"username": "bob", "age":25},
        3: {"username": "mary", "age":52}
    }

    user = users.get(id) # None if not found
    if user is None:
        # a user was not found
        return render(request, "not_found.html", {'error':f"user w id {id} not found"} )
    else:
        return render(request, "profile.html", {"user":users[id]})
