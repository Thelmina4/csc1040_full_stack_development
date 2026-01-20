from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

# profile/1 -> alice
# profile/2 -> bob
def profile(request, id):
    users = {
        1: {"username": "alice", "age":30},
        2: {"username": "albobice", "age":25}
    }

    user = users.get(id) # None if not found
    if user is None:
        #a user was not found
        return render(request, "not_found.html", {'error':f"user w id {id} not found"} )
    else:
        return render(request, "profile.html", {"user":users[id]})
