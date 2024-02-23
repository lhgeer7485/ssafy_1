from django.shortcuts import render

# Create your views here.
foods = ["피자","치킨","국밥","초밥", "민초흑당로제마라탕"]
drinks = ["cider","coke","miranda","fanta", "eye of finetree"]

def drink(request):
    context = {
        'food' : foods,
        'drink' : drinks,
    }
    return render(request, 'menus/drink.html', context)

def food(request):
    context = {
        'food' : foods,
        'drink' : drinks,
    }
    return render(request, 'menus/food.html', context)

def receipt(request):
    n1 = request.GET.get('n1')

    context = {
        'food' : foods,
        'drink' : drinks,
        'n1' : n1
    }
    return render(request, 'menus/receipt.html', context)