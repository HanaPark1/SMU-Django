from django.shortcuts import render, redirect
from students.models import Student

# Create your views here.

def write(request):
    if request.method == 'GET':
        return render(request, 'write.html')
    else:
        name = request.POST.get('name')
        major = request.POST.get('major')
        grade = request.POST.get('grade')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        Student(name=name,major=major,grade=grade,age=age,gender=gender).save()
        return redirect('/students/list/')

def list(request):
    qs = Student.objects.all()
    context = {'list':qs}
    return render(request, 'list.html', context)

def view(request, name):
    qs = Student.objects.get(name=name)
    context = {'stu':qs}
    return render(request, 'view.html', context)

def update(request, name):
    qs = Student.objects.get(name=name)
    if request.method == "GET":
        context = {'stu':qs}
        return render(request, 'update.html', context)
    else:
        name2 = request.POST.get('name')
        major = request.POST.get('major')
        grade= request.POST.get('grade')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        
        qs.name = name2
        qs.major = major
        qs.grade = grade
        qs.age = age
        qs.gender = gender
        
        qs.save()
        return redirect('/students/list/')

def delete(request, name):
    qs = Student.objects.get(name=name)
    qs.delete()
    return redirect('/students/list/')    