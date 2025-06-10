from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import F,Q #F: 검색된 모든 데이터 적용 | Q: 쿼리
from board.models import Board

## 게시판리스트
def list(request):
    # 페이지네이터 사용 시 항상 페이지 번호 필요
    page = int(request.GET.get('page', 1))
    qs = Board.objects.all().order_by('-ntchk', '-bgroup', 'bstep')
    # 하단 넘버링 부분
    paginator = Paginator(qs, 10) # 열개씩 분리해서 가져옴 1,2,3,...,9,10
    list = paginator.get_page(page) # 1페이지 가져오기
    # -----------------
    context = {'list':list, 'page':page}
    return render(request,'board/list.html',context)

## 글쓰기 - get,post
def write(request):
    if request.method == 'GET':
        return render(request,'board/write.html')
    elif request.method == 'POST':
        id = request.POST.get('id')
        # id = request.session.get('session_id') # session에서 가져오기
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        bfile = request.FILES.get('bfile','')
        ntchk = request.POST.get('ntchk',0)
        print("넘어온 데이터 : ",id,btitle,bcontent,bfile,ntchk)
        qs = Board.objects.create(id=id,btitle=btitle,bcontent=bcontent,bfile=bfile,ntchk=ntchk)
        return redirect('/board/list/')
    
def view(request, bno):
    # 현재글
    qs = Board.objects.filter(bno=bno)
    
    # 이전글
    pre_qs = Board.objects.filter(
       Q(ntchk__lte=qs[0].ntchk,bgroup__lt=qs[0].bgroup,bstep__lte=qs[0].bstep)|
       Q(ntchk=qs[0].ntchk,bgroup__lt=qs[0].bgroup)
    ).order_by('-ntchk','-bgroup','bstep').first()
    # 다음글
    next_qs = Board.objects.filter(
       Q(ntchk__gte=qs[0].ntchk,bgroup__gt=qs[0].bgroup,bstep__gte=qs[0].bstep)|
       Q(ntchk__gt=qs[0].ntchk)
    ).order_by('ntchk','bgroup','-bstep').first()
    print('현재글 : ',qs[0].bno)
    print('이전글 : ',pre_qs.bno)
    print('다음글 : ',next_qs.bno)
    context = {'board':qs[0],'pre_board':pre_qs,'next_board':next_qs}
    
    return render(request, 'board/view.html', context)