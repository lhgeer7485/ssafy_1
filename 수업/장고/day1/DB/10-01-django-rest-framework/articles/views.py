from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Article
from .serlializers import ArticleListSerializer

@api_view(['GET'])
def article_list(request):
    articles = Article.objects.all()
    serializer = ArticleListSerializer(articles, many="True")
    return Response(serializer.data)