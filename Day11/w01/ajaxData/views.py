from django.shortcuts import render
from board.models import Board
from . import JsonResponse

# Create your views here.

def bwrite(request):
    id = request.POST.get('id')
    btitle = request.POST.get('btitle')
    bcontent = request.POST.get('bcontent')
    
    # save DB
    qs = Board.objects.create(id=id,btitle=btitle,bcontent=bcontent)
    qs.bgroup = qs.bno
    qs.save()
    
    #trans JSON
    l_qs = list(Board.objects.filter(bno=qs.bno).values())
    print(l_qs)
    
    context = {'result':'success'}
    return JsonResponse(context)
    