from django.shortcuts import render, redirect
from students.models import Student
from datetime import datetime

# Create your views here.

def list(request):
    qs = Student.objects.all()
    context = {'list':qs}
    return render(request, 'list.html', context)

def write(request):
    if request.method == 'GET':
        return render(request, 'write.html')
    else:
        name = request.POST.get('name')
        major = request.POST.get('major')
        grade = request.POST.get('grade')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        hobbys = request.POST.getlist('hobby')
        # 리스트타입 -> str 타입으로 변경
        hobby = ','.join(hobbys)
        
        Student(name=name,major=major,grade=grade,age=age,gender=gender,memo='등록합니다.',hobby=hobby).save()
        return redirect('/students/list')
def view(request,no):
    try:
        qs = Student.objects.get(no=no)
    except:
        qs = None    
    context = {'stu':qs}
    return render(request,'view.html',context)

def update(request, no):
    qs = Student.objects.get(no=no)
    if request.method == "GET":
        context = {'stu':qs}
        return render(request, 'update.html', context)
    else:
        name = request.POST.get('name')
        major = request.POST.get('major')
        grade = request.POST.get('grade')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        hobbys = request.POST.getlist('hobby')
        hobby = ','.join(hobbys)
        
        qs.name = name
        qs.major = major
        qs.grade = grade
        qs.age = age
        qs.gender = gender
        qs.hobby = hobby
        qs.save()
        
        return redirect('/students/list/')
    
def delete(request, no):
    qs = Student.objects.get(no=no)
    qs.delete()
    
    return redirect('/students/list/')