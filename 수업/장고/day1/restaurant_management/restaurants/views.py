from django.shortcuts import render, redirect
from .models import Restaurant
from .forms import RestaurantForm

# Create your views here.

def index(request):
    restaurants = Restaurant.objects.all()
    context = {
        'restaurants' : restaurants
    }
    return render(request, 'restaurants/index.html', context)

def new(request):
    form = RestaurantForm()
    context = {
        'form' : form
    }
    return render(request, 'restaurants/new.html', context)

def create(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            restaurant = form.save()
            return redirect('restaurants:index')
        
    else:
        form = RestaurantForm()

    context = {
        'form' : form
    }

    return render(request, 'restaurants/new.html', context)


def detail(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    context = {
        'restaurant' : restaurant
    }

    return render(request, 'restaurants/detail.html', context)


def edit(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    form = RestaurantForm()

    context = {
        'restaurant' : restaurant,
        'form' : form,
    }

    return render(request, 'restaurants/edit.html', context)


def update(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    if request.method == 'POST':
        form = RestaurantForm(request.POST, instance=restaurant)
        if form.is_valid():
            form.save()
            return redirect('restaurants:index')

    else:
        form = RestaurantForm()

    context = {
        'form' : form
    }

    return render(request, 'restaurants/edit.html', context)


def delete(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    restaurant.delete()
    return redirect('restaurants:index')