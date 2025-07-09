from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('competitions/', views.competitions, name='competitions'),
    path('find-competitions/', views.find_competitions, name='find_competitions'),
    path('find-internships/', views.find_internships, name='find_internships'),
    path('find-a-mentor/', views.find_a_mentor, name='find_a_mentor'),
    path('jobpage/', views.jobpage, name='jobpage'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('mentor-page/', views.mentor_page, name='mentor_page'),
    path('more-courses/', views.more_courses, name='more_courses'),
    path('profile/', views.profile_sidebar, name='profile_sidebar'),
    path('findjob/', views.findjob, name='findjob'),
    path('internship/', views.internship, name='internship'),
    path('hackathon/', views.hackathon, name='hackathon'),

]
