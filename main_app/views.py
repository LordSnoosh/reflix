from django.shortcuts import render, redirect
from django.core.validators import validate_email
from .models import User

# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):
    if User.objects.filter(email = request.POST['email']):
        message = 'You are already signed up.'
        return render(request, 'home.html', { 'message' : message })
    User.objects.create( name = request.POST['name'], email = request.POST['email'])
    message = 'Thank you for signing up.'
    return render(request, 'home.html', { 'message' : message })

def dashboard(request):
    users = User.objects.all()
    return render(request, 'dashboard.html', { 'users' : users })
