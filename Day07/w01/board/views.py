from django.shortcuts import render, redirect
from board.models import Board

# Create your views here.

def list(request):
    qs = Board.objects.all()
    context = {'list':qs}
    return render(request, 'notice_list.html',context)

def write(request):
    if request.method == 'GET':
        return render(request, 'write.html')    
    elif request.method == 'POST':
        id = 'aaa'
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        bfile = request.POST.get('bfile')
        qs = Board.objects.create(id=id,btitle=btitle,bcontent=bcontent)
        qs.bgroup = qs.bno
        qs.save()
        print('데이터 확인 : ',btitle,bcontent,bfile)
        print('데이터추가 : ',qs.bgroup,qs.bstep,bfile)
        return redirect('board:list', orgs={})
    
def view(request, bno):
    qs = Board.objects.get(bno=bno)
    context = {'item':qs}
    return render(request, 'notice_read.html', context)

def update(request, bno):
    qs = Board.objects.get(bno=bno)
    if request.method == 'GET':
        context = {'item':qs}
        return render(request, 'update.html', context)
    elif request.method == 'POST':
        id = request.session['session_id']
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        bfile = request.POST.get('bfile')
        
        print(id, btitle, bcontent)
        qs.btitle = btitle
        qs.bcontent = bcontent
        qs.save()
        
        return redirect('/board/list/')