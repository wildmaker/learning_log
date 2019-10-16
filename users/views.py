from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login
def userlogin(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username = username, password = password)
    if user is not None:
        login(request, user)
        # redirect
    else:
        # return an error message