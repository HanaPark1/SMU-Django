from django.shortcuts import render, redirect
from board.models import Board

# Create your views here.

def list(request):
    qs = Board.objects.all()
    context = {'list':qs}
    return render(request, 'list.html', context)

def write(request):
    if request.method == 'GET':
        return render(request, 'write.html')
    elif request.method == 'POST':
        id = request.session['session_id']
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        bfile = request.POST.get('bfile')
        print(id, btitle, bcontent, bfile)
        Board(id=id, btitle=btitle, bcontent=bcontent).save()
        
        return redirect('/board/list/')
    
def view(request, bno):
    qs = Board.objects.get(bno=bno)
    context = {'item':qs}
    return render(request, 'read.html', context)