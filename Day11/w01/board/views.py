from django.shortcuts import render, redirect
from django.http import JsonResponse
from board.models import Board
from django.core import serializers # json타입으로 변경

# Create your views here.

def list(request):
    if request.method == 'GET':
        qs = Board.objects.all().order_by('-ntchk', '-bgroup', 'bstep')
        context = {'list':qs}
        return render(request, 'list.html', context)
    elif request.method == 'POST':
        id = request.POST.get('id')
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        print('넘어온 데이터!: ',id,btitle,bcontent)
        
        qs = Board.objects.create(id=id, btitle=btitle, bcontent=bcontent)
        qs.bgroup = qs.bno
        qs.save()
        return redirect('/board/list/')
    
def list2(request):
    if request.method == 'GET':
        qs = Board.objects.all().order_by('-ntchk', '-bgroup', 'bstep')
        context = {'list':qs}
        return render(request, 'list2.html', context)
    elif request.method == 'POST':
        id = request.POST.get('id')
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        print('넘어온 데이터!: ',id,btitle,bcontent)
        
        qs = Board.objects.create(id=id, btitle=btitle, bcontent=bcontent)
        qs.bgroup = qs.bno
        qs.save()
        return redirect('/board/list2/')
    
def list3(request):
    qs = Board.objects.all().order_by('-ntchk','-bgroup','bstep')
    context = {'list':qs}
    return render(request,'board/list3.html',context)
    
def view(request):
    bno = request.GET.get('bno')
    qs = Board.objects.get(bno=bno)
    context = {'board':qs}
    return render(request, 'view.html', context)

def view2(request, bno):
    qs = Board.objects.get(bno=bno)
    context = {'board':qs}
    return render(request, 'view.html', context)

# Board 모든 데이터 가져오기
def ajax3(request):
    qs = Board.objects.all().order_by('-ntchk','-bgroup','bstep')
    print(qs)
    a = request.POST.get('sampleId')
    print('넘어온 데이터 : ',a)
    list_qs = serializers.serialize('json',qs)   
    print("변경타입 : ",list_qs)
    context = {'result':'성공','list':list_qs}
    return JsonResponse(context)