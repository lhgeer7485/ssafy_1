from django.shortcuts import render

# Create your views here.
def first(request):
    context = {
    'message' : request.GET.get('message')
    }
    return render(request, 'throw_catch/first.html', context)

def second(request):
    # if len(request.GET.get('message')) == 0:
    #     message = None

    context = {
        'message' : request.GET.get('message')
    }
    return render(request, 'throw_catch/second.html', context)