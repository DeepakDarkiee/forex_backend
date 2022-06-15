from django.urls import path

from journal import views

urlpatterns = [
    path("volume/", views.VolumeGetPostView.as_view(), name="volume"),
    path("volume/<int:id>", views.VolumePutDeleteView.as_view(), name="volume"),
    
    path("issues/", views.IssueView.as_view(), name="issues"),
    path("issues/<int:id>", views.IssuePutDeleteView.as_view(), name="issues"),
    
    
    path("apc/", views.APCView.as_view(), name="apc"),
    path("apc/<int:id>", views.APCPutDeleteView.as_view(), name="apc"),
    
    path("journal_matrix/", views.JournalMatrixView.as_view(), name="journal_matrix"),
    path("journal_matrix/<int:id>", views.JournalMatrixPutDeleteView.as_view(), name="journal_matrix"),    
    
    
    path("journals/", views.JournalsView.as_view(), name="journals"),
    path("journals/<int:id>", views.JournalsPutDeleteView.as_view(), name="journals"),    
    
    
    path("artical/", views.ArticleView.as_view(), name="artical"),
]
