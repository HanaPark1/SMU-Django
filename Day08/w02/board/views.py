from django.shortcuts import render, redirect
from board.models import Board

# Create your views here.

def list(request):
    qs = Board.objects.all()
    context = {'list':qs}
    return render(request, 'notice_list.html', context)


def write(request):
    if request.method == 'GET':
        return render(request, 'write.html')
    elif request.method == 'POST':
        # id = request.POST.get('id')
        id = 'aaa'
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        bfile = request.POST.get('bfile')
        Board(id=id,btitle=btitle,bcontent=bcontent,bfile=bfile).save()
        return redirect('/board/list/')
    
def view(request, bno):
    qs = Board.objects.get(bno=bno)
    context = {'board':qs}
    return render(request, 'notice_read.html', context)

def update(request, bno):
    qs = Board.objects.get(bno=bno)
    if request.method == 'GET':
        context = {'board':qs}
        return render(request, 'update.html', context)
    elif request.method == 'POST':
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        bfile = request.POST.get('bfile','')
        
        qs.btitle = btitle
        qs.bcontent = bcontent
        qs.bfile = bfile
        qs.save()
        return redirect('/board/list/')
    
def delete(request, bno):
    Board.objects.get(bno=bno).delete()
    return redirect('/board/list/')

def reply(request, bno):
    qs = Board.objects.get(bno=bno)
    if request.method == 'GET':
        context = {'board':qs}
        return render(request, 'reply.html', context)
    elif request.methon == 'POST':
        id = request.POST.get('id')
        bgroup = request.POST.get('bgroup')
        bstep = int(request.POST.get('bstep'))
        bindent = int(request.POST.get('bindent'))
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        bfile = request.FILES.get('bfile')
        
        