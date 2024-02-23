from django.shortcuts import render

# Create your views here.
def calculators(requests, num1, num2):

    sub = num1 - num2
    mul = num1 * num2
    div = 0
    if num2 != 0:
        div = num1 / num2
    
    context = {
        'num1' : num1,
        'num2' : num2,
        'sub' : sub,
        'mul' : mul,
        'div' : div,
    }



    return render(requests, 'calculators/calculators.html', context)