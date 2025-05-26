from django.shortcuts import render
from django.http import HttpResponse
from students.models import Student


# Create your views here.
def list(request):
    # HttpResponse : 글자를 http파일로 변경해서 출력
    qs = Student.objects.all()
    context = {'list':qs}
    print(qs)
    return render(request, 'list.html',context)
    # return render(request,'list.html')
def view(request):
    name = '유관순'
    qs = Student.objects.get(name=name)
    context={'stu':qs}
    print(qs)
    return render(request, 'view.html',context)

