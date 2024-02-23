from django.shortcuts import render

# Create your views here.
def first(request):
    context = {
        'n1' : request.GET.get('message1'),
    }
    return render(request, 'throw_loops/first.html', context)

def second(request):
    context = {
        'n1' : request.GET.get('message1'),
    }
    return render(request, 'throw_loops/second.html',context)

def third(request):
    context = {
        'n1' : request.GET.get('message1'),
        'n2' : request.GET.get('message2')
    }
    return render(request, 'throw_loops/third.html', context)
