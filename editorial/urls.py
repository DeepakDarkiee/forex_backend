from django.urls import path

from editorial import views

urlpatterns = [
    path("artical/", views.ArticleView.as_view(), name="artical"),
]