from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from students.models import Student, Student2
from django.urls import reverse

# Create your views here.

def list(request):
    qs = Student2.objects.all()
    # qs = Student.objects.all()
    context = {'list':qs}
    return render(request, 'list.html', context)

def write(request):
    return render(request, 'write.html')

def write2(request):
    #request.POST[], request.POST.get()
    name = request.POST.get('name')
    major = request.POST.get('major')
    age = request.POST.get('age')
    grade = request.POST.get('grade')
    gender = request.POST.get('gender')
    print(name)
    qs = Student2(name=name, major=major, age=age, grade=grade, gender=gender)
    qs.save()
    # redirect('앱네임:url이름')
    return redirect('students:list') #앱 이름
    # return redirect('students/list') 앱 url
    # return HttpResponseRedirect(reverse('students:list'))