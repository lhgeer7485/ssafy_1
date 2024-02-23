from django.shortcuts import render

# Create your views here.
def fruits(request):
    return render(request, 'fruits/fruits.html')