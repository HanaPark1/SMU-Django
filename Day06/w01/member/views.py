from django.shortcuts import render,redirect
from member.models import Member

# Create your views here.

def login(request):
    if request.method == "GET" :
        return render(request, 'login.html')
    elif request.method == "POST":
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        try :
            qs = Member.objects.get(id=id)
            if qs.pw == pw:
                # 세션 할당
                request.session['session_id'] = id
                txt = 1
            else:
                txt = -1 # 아이디 존재, 비번 오류
        except:
            txt = 0 # 아이디가 없음
            
        # try :
        #     qs = Member.objects.get(id=id, pw=pw)
        #     # 세션 할당
        #     request.session['session_id'] = id
        #     txt = 1
        # except:
        #     txt = 0
        context = {'msg':txt}
        return render(request, 'login.html', context)

def logout(request):
    # 세션 삭제
    # request.session.clear() #모두삭제
    # del request.session['session_id'] # 세션 하나 삭제
    del request.session['session_id']
    return redirect('/')