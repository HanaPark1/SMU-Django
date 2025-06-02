from django.shortcuts import render, redirect
from member.models import Member

# Create your views here.

def login(request):
    if request.method == 'GET':
        save_id = request.COOKIES.get('idCheck', '')
        context = {'save_id':save_id}
        return render(request, 'login.html', context)
    else:
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        save_id = request.POST.get('idCheck')
        print(id, pw)
        
        try:
            qs = Member.objects.get(id=id, pw=pw)
        except:
            context = {'msg': 0}
            return render(request, 'login.html', context)
        
        request.session['session_id'] = id
        
        response = redirect('/')
        
        if(save_id != None):
            response.set_cookie('idCheck',id)
        else:
            response.delete_cookie('idCheck')
            
        return response
    
def logout(request):
    del request.session['session_id']
    return redirect('/')