from django.shortcuts import render

def home(request):
    return render(request, 'final_home_page_2.html')

def competitions(request):
    return render(request, 'competitions_page.html')

def find_competitions(request):
    return render(request, 'find_competitions_page.html')

def find_internships(request):
    return render(request, 'find_internships_page.html')

def find_a_mentor(request):
    return render(request, 'find_a_mentor.html')

def jobpage(request):
    return render(request, 'jobpage.html')

def login(request):
    return render(request, 'loginpage.html')

def register(request):
    return render(request, 'reg_page.html')

def mentor_page(request):
    return render(request, 'mentor_page.html')

def more_courses(request):
    return render(request, 'more_courses.html')

def profile_sidebar(request):
    return render(request, 'another_profile_slidebar.html')

def findjob(request):
    return render(request, 'findjob.html')

def internship(request):
    return render(request, 'internship_page.html')
def hackathon(request):
    return render(request, 'hackathon.html')
