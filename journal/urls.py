from django.urls import path

from journal import views

urlpatterns = [
    path("volume/", views.VolumeGetPostView.as_view(), name="volume"),
    path("volume/<int:id>/", views.VolumePutDeleteView.as_view(), name="volume"),
    
    path("issues/", views.IssueView.as_view(), name="issues"),
    path("issues/<int:id>/", views.IssuePutDeleteView.as_view(), name="issues"),
    
    
    path("apc/", views.APCView.as_view(), name="apc"),
    path("apc/<int:id>/", views.APCPutDeleteView.as_view(), name="apc"),
    
    path("journal/matrix/", views.JournalMatrixView.as_view(), name="journal_matrix"),
    path("journal/matrix/<int:id>/", views.JournalMatrixPutDeleteView.as_view(), name="journal_matrix"),    
    
    
    path("journals/", views.JournalsView.as_view(), name="journals"),
    path("journals/<int:id>/", views.JournalsPutDeleteView.as_view(), name="journals"),    
    
    
    
    path("page/number/", views.PageNumberView.as_view(), name="pagenumber"),
    path("page/number/<int:id>/", views.PageNumberPutDeleteView.as_view(), name="page_number"),    
    
    
    path("article/type/", views.ArticleTypeView.as_view(), name="articletype"),
    path("article/type/<int:id>/", views.ArticleTypePutDeleteView.as_view(), name="article_type"),  
    
    # path("scope/type/", views.ScopeTypeView.as_view(), name="scopetype"),
    # path("scope/type/<int:id>/", views.ScopeTypePutDeleteView.as_view(), name="scope_type"),  
    
]
