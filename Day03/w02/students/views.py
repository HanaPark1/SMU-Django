from django.shortcuts import render, redirect
from students.models import Student
# Create your views here.

def list(request):
    qs = Student.objects.all()
    context = {'list':qs}
    return render(request, 'students/list.html', context)


def write(request):
    return render(request, 'students/write.html')

def writeOK(request):
    name = request.POST.get('name')
    major = request.POST.get('major')
    age = request.POST.get('age')
    grade = request.POST.get('grade')
    gender = request.POST.get('gender')
    print(name,major,age,grade,gender)
    
    qs = Student(name=name,major=major,age=age,grade=grade,gender=gender)
    qs.save()
    return redirect("students:list")