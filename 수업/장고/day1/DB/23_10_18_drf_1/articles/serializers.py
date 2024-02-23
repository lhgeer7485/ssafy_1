from rest_framework import serializers
from .models import Article

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'id', 'content')



class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'