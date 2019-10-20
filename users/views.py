from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from django.contrib.auth import authenticate, login, logout
def userlogin(request):
    """用户登录"""
    if request.method != "POST":
        context = {}
    else:
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username = username, password = password)
        print(user)
        if user is not None:
            login(request, user)
            # redirect
            print("heihei222")
            return HttpResponseRedirect(reverse("learning_logs:index"))
        else:
            # return an error message
            context = {"error_message":"login error"}
        
    return render(request,'users/login.html', context)


# 注销
def userlogout(request):
    """注销用户"""
    logout(request)
    return HttpResponseRedirect(reverse("learning_logs:index"))