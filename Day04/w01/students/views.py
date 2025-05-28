from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from students.models import Student
# Create your views here.

def write(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        major = request.POST.get('major')
        grade = request.POST.get('grade')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        print('입력된 정보: ',name,major,grade,age,gender)
        Student(name=name,major=major,grade=grade,gender=gender,age=age).save()
        return redirect('/students/list')
    else:
        print("request: ", request)
        print("request get: ", request.GET)
        print("request method: ", request.method)
        return render(request,'write.html')

def list(request):
    #DB 검색
    # objects.all() - 전체 가져오기 | objects.get() - 해당하는 것 선택 가져오기 | objects.filter() - 검색 | objects.order_by() - 정렬, (-) - 역순정렬
    # objects.filter() - 검색 - __contains -> 포함 | __gte -> 같거나 더 크다 | __gt -> 크다 | __lt -> 작다 | __lte -> 작거나 같다
    qs = Student.objects.order_by('-name')
    context = {'list':qs}
    return render(request, 'list.html', context)

def view(request):
    name = request.GET.get('name')
    qs = Student.objects.get(name=name)
    print(qs)
    context = {'stu':qs}
    # print("전달 이름: ", name)
    return render(request, 'view.html', context)

def update(request, name):
    qs = Student.objects.get(name=name)
    if request.method == 'GET':
        context = {'stu':qs}
        return render(request, 'update.html',context)
    else:
        name2 = request.POST.get('name')
        major = request.POST.get('major')
        grade = request.POST.get('grade')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        
        qs.name = name2
        qs.major = major
        qs.grade = grade
        qs.age = age
        qs.gender = gender
        qs.save()
        return redirect('/students/list')
    
def delete(request, name):
    qs = Student.objects.get(name=name)
    qs.delete()
    return redirect('/students/list')