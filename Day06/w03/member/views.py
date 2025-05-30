from django.shortcuts import render, redirect
from member.models import Member

# Create your views here.

def login(request):
    cookie_info = request.COOKIES
    cook_id = cookie_info.get('cookie_val')
    print("cookid: ",cook_id)
    context = {'cookie_info':cookie_info,'cook_id':cook_id}
    
    if request.method == 'GET':
        return render(request, 'login.html', context)
    
    elif request.method == 'POST' : 
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        cookie_val = request.POST.get('cookie_val')
        try:
            qs = Member.objects.get(id=id, pw=pw)
            if qs.pw ==  pw:
                txt = 1
                request.session['session_id'] = id
                request.session['session_nickName'] = qs.nickName
            else:
                txt = -1
        except:
            txt = 0

        context = {"msg":txt, 'cookie_info':cookie_info}
                
        response = render(request, 'login.html', context, cook_id)
        # response 쿠키 저장
        if cookie_val is not None:
            #cookie_val = 'idsave'
            response.set_cookie('cookie_val', id, max_age=60*60*24*365) #(60초 * 60분 * 24시간 * 365일)
        else:
            response.delete_cookie('cookie_val')
        return response

def logout(request):
    del request.session['session_id']
    return redirect('/')