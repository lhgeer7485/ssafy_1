from rest_framework import serlializers

from .models import Article

class ArticleListSerializer(serlializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)