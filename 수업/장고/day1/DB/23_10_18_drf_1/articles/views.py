from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework import status
from .models import Article
from rest_framework.decorators import api_view
from .serializers import ArticleListSerializer, ArticleSerializer


@api_view(['GET'])
def article_list(request):
    articles = Article.objects.all()
    serializer = ArticleListSerializer(articles, many=True)

    return Response(serializer.data)

@api_view()
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    serializer = ArticleSerializer(article)

    return Response(serializer.data)