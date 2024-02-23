from django.shortcuts import render

# Create your views here.
def calculation(request):
    return render(request, 'calculators/calculation.html')

def result(request):

    n1 = int(request.GET.get('n1'))
    n2 = int(request.GET.get('n2'))

    mul = n1 * n2
    sub = n1 - n2
    if n2 == 0:
        div = None
    else:
        div = n1 / n2

    context = {'n1' : n1,
               'n2' : n2,
               'mul' : mul,
               'sub' : sub,
               'div' : div,
               }
    return render(request, 'calculators/result.html', context)
