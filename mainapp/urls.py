from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register_html'),
    path('register/', views.register, name='register'),
    path('home', views.home, name='home_html'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),  
    path('profile/', views.profile, name='profile'),
    path('competitions/', views.competitions, name='competitions'),
    path('findjob/', views.find_job, name='find_job'),
    path('find-mentor/', views.find_mentor, name='find_mentor'),
    path('find-competitions/', views.find_competitions, name='find_competitions'),
    path('find-internships/', views.find_internships, name='find_internships'),
    path('hackathon/', views.hackathon, name='hackathon'),
    path('internships/', views.internships, name='internships'),
    path('jobs/', views.jobs, name='jobs'),
    path('mentorships/', views.mentorships, name='mentorships'),
    path('more/', views.more, name='more'),
    path('courses/', views.courses, name='courses'),
    path('practice/', views.practice, name='practice'),
    path('boostyourknowledge/', views.boostyourknowledge, name='boostyourknowledge'),
]
# This file defines the URL patterns for the core application of the Unstop clone project.
# Each path corresponds to a view function that renders a specific template.
