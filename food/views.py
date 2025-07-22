from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Food
from .forms import FoodForm

def food_list(request):
    query = request.GET.get('q')
    if query:
        foods = Food.objects.filter(name__icontains=query)
    else:
        foods = Food.objects.all()
    return render(request, 'food_list.html', {'foods': foods})

@login_required
def add_food(request):
    if request.method == 'POST':
        form = FoodForm(request.POST, request.FILES)
        if form.is_valid():
            food = form.save(commit=False)
            food.author = request.user
            food.save()
            form.save_m2m()
            return redirect('food_list')
        else:
            print(form.errors) 
    else:
        form = FoodForm()
    return render(request, 'add_food.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('food_list')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


# Create your views here.
