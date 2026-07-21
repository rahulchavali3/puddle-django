from django.shortcuts import render, redirect
from item.models import Category,Item
from .forms import SignupForm
from .forms import ContactMessageForm

def index(request):
    items = Item.objects.filter(is_sold = False)[0:6]
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'categories' : categories,
        'items' : items,
    })

def contact(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)

        if form.is_valid():
            form.save()

    else:
        form = ContactMessageForm()

    return render(request, 'core/contact.html', {
        'form': form
    })

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

def about(request):
    return render(request, 'core/about.html')

def policy(request):
    return render(request, 'core/policy.html')