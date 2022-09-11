from django.urls import path

from editorial import views
from editorial.article_activity.apis import ArticleActivityView, SingleArticleActivityView

urlpatterns = [
    path("article/", views.ArticleView.as_view(), name="artical"),
    path("single/article/<int:id>/", views.SingleArticleView.as_view(), name="single_artical"),

    path("article/activity/",ArticleActivityView.as_view(), name="article_activity"),
    path("single/article/activity/<int:id>/",SingleArticleActivityView.as_view(), name="single_article_activity"),



]