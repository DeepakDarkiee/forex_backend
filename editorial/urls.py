from django.urls import path

from editorial.author_rights import apis

urlpatterns = [
    path("article/", apis.ArticleView.as_view(), name="artical"),
    path("single/article/<int:id>/", apis.SingleArticleView.as_view(), name="single_artical"),

]