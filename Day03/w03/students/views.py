from django.shortcuts import render

# Create your views here.

def list(request):
    id = request.POST.get('id')
    pw = request.POST.get('pw')
    gender = request.POST.get('gender')
    tel = request.POST.get('tel')
    hobbys = request.POST.getlist("hobby")
    context = {"id":id, "pw":pw, "gender":gender,'tel':tel,'hobby':hobbys}
    return render(request, 'list.html', context)

def view(request):
    name = request.GET.get('name')
    age = request.GET.get('age')
    context = {'name':name, 'age':age}
    return render(request,'view.html', context)

def write(request):
    return render(request,'write.html')

def result(request):
    name = request.POST.get('name')
    kor = int(request.POST.get('kor'))
    eng = int(request.POST.get('eng'))
    total = kor+eng
    hobbys = request.POST.getlist('hobby')
    print(name,kor,total)
    context = {'name':name,'kor':kor,'eng':eng,'total':total,'hobby':hobbys}
    return render(request,'result.html',context)

def send(request,name,age):
    context = {'name':name, 'age':age}
    return render(request, 'send.html',context)