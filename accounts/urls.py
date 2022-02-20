from accounts.author.api import (RegisterAuthorView,LoginAuthorAPIView)
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("register_author/", RegisterAuthorView.as_view(), name="register_author"),
    path("login_author/", LoginAuthorAPIView.as_view(), name="login_author"),
    
]
