from django.shortcuts import render
from .models import Article
# Create your views here.
def index(request):

    articles = Article.objects.all()

    content = {
        'articles' : articles
    }

    return render(request, 'articles/index.html', content)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    article = Article(title= title, content= content)
    article.save()
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)

def delete(request, pk):
    instance = Article.objects.get(pk=pk)
    instance.delete()
    
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)