from multiprocessing import context
from django.shortcuts import render
from .models import Student


def index(request):
    return render(request, 'fscohort/index.html')


def student_list(request):
    students = Student.objects.all()
    context = {
        "student": students
    }
    return render(request, "fscohort/student_list.html", context)
