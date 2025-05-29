from django.shortcuts import render,redirect
from students.models import Student

# Create your views here.

def list(request):
    try:
        qs = Student.objects.all()
    except:
        qs = None
    context = {"list":qs}
    return render(request, 'list.html', context)

def write(request):
    return render(request, 'write.html')

def writeOK(request):
    name = request.POST.get('name')
    major = request.POST.get('major')
    grade = request.POST.get('grade')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    
    Student(name=name,major=major,grade=grade,age=age,memo='등록',gender=gender).save()
    
    return redirect('/students/list/')


    
    