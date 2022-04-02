from django.urls import path
from journal import views

urlpatterns = [
path('volumes/',views.VolumeView.as_view(),name='volumes'),
path('issues/',views.IssueView.as_view(),name='issues'),
path('apc/',views.APCView.as_view(),name='apc'),
path('journal_matrix/',views.JournalMatrixView.as_view(),name='journal_matrix'),
path('journals/',views.JournalsView.as_view(),name='journals')
]   