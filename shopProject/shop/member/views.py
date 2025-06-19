from django.shortcuts import render
from member.models import Member

# Create your views here.

def login(request):
    if request.method == "GET":
        return render(request, 'member/login.html') 
    elif request.method == "POST":
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        idsave = request.POST.get('idsave')
        print('아이디, 비번, 아이지저장: ',id, pw, idsave)
        
        ##db확인
        qs = Member.objects.filter(id=id,pw=pw) # None
        if Member.objects.filter(id=id,pw=pw):
            msg = '1'
            request.session['session_id'] = id
            request.session['session_name'] = qs[0].name
            
        else:
            msg = '0'
        context = {'msg':msg}
        response = render(request, 'member/login.html', context)
        if idsave:
            response.set_cookie('cook_id',id,max_age=60*60*24*14)
        else:
            response.delete_cookie('cook_id')
        return response

def step01(request):
    return render(request, 'member/step01.html')