from django.shortcuts import render
from .models import Student


# Create your views here.

def cohort_home(request):
    # return HttpResponse('welcome to my come')
    students = Student.objects.all()
    

    return render(request, "student/index.html", {
        'students': students
    })


def about_cohort(request):
    
    return render(request, "student/about.html")