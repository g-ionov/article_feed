from rest_framework.permissions import AllowAny
from rest_framework import generics
from .models import Article
from .serializers import ArticleSerializer, ArticleCreateSerializer
from .permissions import IsSubscriber, IsAuthorOrReadOnly, IsAuthor

class ArticlePublicListView(generics.ListAPIView):
    """Просмотр публичных статей"""
    serializer_class = ArticleSerializer
    queryset = Article.objects.filter(for_subscribers=False)
    permission_classes = [AllowAny]

class ArticlePrivateListView(generics.ListAPIView):
    """Просмотр статей для подписчиков"""
    serializer_class = ArticleSerializer
    queryset = Article.objects.filter(for_subscribers=True)
    permission_classes = [IsSubscriber]

class ArticleCreateView(generics.CreateAPIView):
    """Создание статей"""
    serializer_class = ArticleCreateSerializer
    permission_classes = [IsAuthor]

class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Просмотр детальной информации, редактирование, удаление статей"""
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    def get_permissions(self):
        pk = self.kwargs.get('pk')
        article = Article.objects.get(pk=pk)
        if article.for_subscribers:
            self.permission_classes = [IsSubscriber, IsAuthorOrReadOnly]
        else:
            self.permission_classes = [IsAuthorOrReadOnly]
        return super(ArticleDetailView, self).get_permissions()