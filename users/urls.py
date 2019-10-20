from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^login/$', views.userlogin, name = 'userlogin'),
    re_path(r'^logout/$', views.userlogout, name = 'logout')
]