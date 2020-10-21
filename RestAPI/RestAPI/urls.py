
from django.contrib import admin
from django.urls import path
from API.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", Home, name = "home"),
    path("api/", ListofPosts, name = "home"),
    path("sendMail/", Send_Mail, name = "mail")
]
