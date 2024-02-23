from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def output(request):

    context = {'id' : request.GET.get('id')}


    return render(request, 'articles/output.html', context)