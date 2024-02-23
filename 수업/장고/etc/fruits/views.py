from django.shortcuts import render

# Create your views here.
def fruits(request):

    fruit_list = ["귤","딸기","사과","감","바나나","파인애플","구아바", "복숭아", "망고스틴"]
    hate = ["사과","구아바"]

    context = {'fruits_name' : fruit_list, 'hate' : hate}

    # context = {'username' : request.GET.get('username')}



    return render(request, 'fruits/fruits.html', context)
    


def name_form(request):
    return render(request, 'fruits/throw.html')