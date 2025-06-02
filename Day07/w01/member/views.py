from django.shortcuts import render, redirect
from member.models import Member

# Create your views here.

def login(request):
    if request.method == 'GET':
        # idCheck 되어 있으면, 저장된 아이디를 리턴해서 돌려줌.
        # 모든 쿠키 읽어오기 : request.COOKIES
        # 해당 쿠키 읽어오기
        idCheck = request.COOKIES.get('idCheck', '') # 없으면 '' <- 빈공백처리/
        context = {'save_id' : idCheck}
        return render(request, 'login.html', context)
    elif request.method == 'POST':
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        idCheck = request.POST.get('idCheck') # 있을 수도 있고, 없을 수도 있고
        
        try :
            qs = Member.objects.get(id=id,pw=pw)
        except:
            context = {'msg':0}
            return render(request, 'login.html', context)
        
        # session 저장
        request.session['session_id'] = id
        
        context = {'msg':1}
        # response 쿠키 저장
        response =  redirect('/', )
        if idCheck != None:
            print('idCheck')
            #쿠키에 id를 저장해서 돌려줌
            response.set_cookie('idCheck',id) #쿠키저장
        else:
            print('idCheck가 없음')
            response.delete_cookie('idCheck') #쿠키삭제 
        return response
    
def logout(request):
    del request.session['session_id']
    return redirect('/')

#동의페이지    
def join01(request):
    return render(request, 'join01_terms.html')
        
#회원가입페이지, 회원가입저장
def join02(request):
    if request.method == 'GET':
        return render(request, 'join02_info_input.html')
    elif request.method == 'POST':
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        name = request.POST.get('name')
        nickName = request.POST.get('nickName')
        f_tell = request.POST.get('f_tell')
        m_tell = request.POST.get('m_tell')
        l_tell = request.POST.get('l_tell')
        tel = f"{f_tell}-{m_tell}-{l_tell}"
        gender = request.POST.get('gender')
        hobbys = request.POST.getlist('hobby')
        hobby = ','.join(hobbys)
        print(id, pw,name, nickName, tel, gender, hobby)
        
        Member(name=name,id=id,pw=pw,nickName=nickName,tel=tel,gender=gender,hobby=hobby).save()
        return redirect('/member/join03/')
        
def join03(request):
    return render(request, 'join03_success.html')