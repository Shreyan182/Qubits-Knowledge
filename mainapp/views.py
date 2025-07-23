from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout as auth_logout, authenticate, login as auth_login
from .models import CustomUser
from django.conf import settings
from django.db import IntegrityError

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type', 'student')
        user = authenticate(request, username=username, password=password)
        if user is not None and getattr(user, 'user_type', None) == user_type:
            # If you have a user_type field, check it here. Otherwise, skip this check.
            # Example: if hasattr(user, 'user_type') and user.user_type == user_type:
            auth_login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {
                'error': 'Invalid credentials or user type.'
            })
    return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')  # Not used unless you have a custom user model

        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password,
            user_type=user_type
        )
        user.full_name = request.POST.get('full_name', '')
        user.year_of_study = request.POST.get('year_of_study', '')
        user.college_name = request.POST.get('college_name', '')
        user.save()
        user.backend = settings.AUTHENTICATION_BACKENDS[0]

        auth_login(request, user)
        return redirect('home')
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
