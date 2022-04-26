from rest_framework import serializers
from .models import Article, User

class ArticleSerializer(serializers.ModelSerializer):
    """Сериализация для статьи
    (список публичных, приватных, а также детальная информация)"""
    author = serializers.SlugRelatedField('email', read_only=True)
    created_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M", read_only=True)
    updated_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M", read_only=True)

    class Meta:
        model = Article
        fields = ('title', 'text', 'author', 'created_at', 'updated_at')

class ArticleCreateSerializer(serializers.ModelSerializer):
    """Сериализация для создания статьи"""
    author = serializers.PrimaryKeyRelatedField(many=False, queryset=User.objects.filter(is_author=True))

    class Meta:
        model = Article
        fields = ('title', 'text', 'author', 'for_subscribers')
