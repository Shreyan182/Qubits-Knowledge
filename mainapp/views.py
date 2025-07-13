from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout as auth_logout, authenticate, login as auth_login

def login(request):
    # Example login logic (expand with real authentication as needed)
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        # Get fields from any form/tab
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = email  # Use email as username

        if not email or not password:
            return render(request, 'register.html', {'error': 'Email and password are required.'})

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Email already registered.'})

        user = User.objects.create_user(
            username=email,  # Use email as username
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        user.save()
        # Auto-login after registration
        user = authenticate(request, username=email, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return render(request, 'register.html', {'error': 'Registration successful, but login failed.'})
    return render(request, 'register.html')

def home(request):
    user = request.user
    if user.is_authenticated:
        user_name = user.get_full_name() or user.username
        user_email = user.email
    else:
        user_name = "Guest"
        user_email = ""
    return render(request, 'home.html', {
        'user_name': user_name,
        'user_email': user_email,
    })

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def profile(request):
    user = request.user
    if user.is_authenticated:
        user_name = user.get_full_name() or user.username
        user_email = user.email
    else:
        user_name = "Guest"
        user_email = "Not logged in"
    return render(request, 'profile.html', {
        'user_name': user_name,
        'user_email': user_email,
    })

def competitions(request):
    return render(request, 'competitions.html')

def boostyourknowledge(request):
    return render(request, 'boostyourknowledge.html')

def find_job(request):
    return render(request, 'findjob.html')

def find_mentor(request):
    return render(request, 'find_mentor.html')

def find_competitions(request):
    return render(request, 'find_competitions.html')

def find_internships(request):
    return render(request, 'find_internships.html')

def hackathon(request):
    return render(request, 'hackathon.html')

def internships(request):
    return render(request, 'internships.html')

def jobs(request):
    return render(request, 'jobs.html')

def mentorships(request):
    return render(request, 'mentorships.html')

def more(request):
    return render(request, 'more.html')

def courses(request):
    return render(request, 'courses.html')

def practice(request):
    return render(request, 'practice.html')
