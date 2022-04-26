from django.urls import path
from.views import ArticlePublicListView, ArticlePrivateListView, ArticleCreateView, ArticleDetailView

urlpatterns = [
    path('article/public', ArticlePublicListView.as_view()),
    path('article/private', ArticlePrivateListView.as_view()),
    path('article/create', ArticleCreateView.as_view()),
    path('article/detail/<int:pk>', ArticleDetailView.as_view()),
]
