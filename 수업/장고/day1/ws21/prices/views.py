from django.shortcuts import render

# Create your views here.
def prices(request, thing, cnt):

    product_price = {"라면":980,"홈런볼":1500,"칙촉":2300, "식빵":1800}

    result = 0

    if thing in product_price:
        result = product_price[thing] * cnt

    context = {'result' : result,
               'thing' : thing,
               'cnt' : cnt,
               }

    return render(request, 'prices/prices.html', context)