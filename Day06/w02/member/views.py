from django.shortcuts import render,redirect
from member.models import Member

# Create your views here.
def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        try:
            qs = Member.objects.get(id=id)
            if (qs.pw == pw) :
                request.session['session_id'] = id
                txt = 1
            else:
                txt = -1
        except:
            txt = 0
        context = {'msg' : txt}
        return render(request, 'login.html', context)
    
def logout(request):
    del request.session['session_id']
    return redirect('/')