from multiprocessing import context
import profile
from django.shortcuts import redirect, render

from .forms import StudentForm


def index(request):
    return render(request, 'student/index.html')


def student_page(request):
    # print(request.POST)
    form = StudentForm(request.POST or None)

    if form.is_valid():
        student = form.save()
        if 'profile_pic' in request.FILES:
            student.profile_pic = request.FILES['profile_pic']
            student.save()
        return redirect('index')
        # print(form.cleaned_data.get('first_name'))
    context = {
        'form': form
    }
    return render(request, 'student/student.html', context)
