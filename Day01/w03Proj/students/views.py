from django.shortcuts import render
from students.models import Student

# Create your views here.

def list(request):
    qs = Student.objects.all()
    context = {'list':qs}
    print(qs)
    return render(request, 'list.html', context)

def view(request):
    name = "유관순"
    qs = Student.objects.get(name=name)
    context = {'stu':qs}
    print(qs)
    return render(request, 'view.html', context)
