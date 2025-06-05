from django.shortcuts import render,redirect
from board.models import Board
# F함수사용 - filter검색된 필드에서 특정컬럼의 값을 가져오는 함수
# Q함수 사용 - AND OR NOT 연산자 사용
from django.db.models import F, Q
from django.core.paginator import Paginator

# 게시글쓰기 - 게시글페이지열기, 게시글저장
def write(request):
    if request.method == "GET":
        return render(request,'write.html')
    elif request.method == "POST":
        # 데이터 가져오기
        id = request.POST.get('id') #섹션에서 가져옴.
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        bfile = request.POST.get('bfile')
        print('write 가져온 데이터 : ',id,btitle,bcontent,bfile)
        # 1.save() 저장
        # Board(id=id,btitle=btitle,bcontent=bcontent,bfile=bfile).save()
        # 2.create저장
        qs = Board.objects.create(id=id,btitle=btitle,bcontent=bcontent,bfile=bfile)
        qs.bgroup = qs.bno
        qs.save()
        context = {'msg':1}
        return render(request,'write.html',context)

# 게시글보기
def view(request,bno):
    # 1.qs값 수정
    # qs = Board.objects.get(bno=bno)
    # qs.bhit += 1
    # qs.save()
    # context = {'board':qs}
    category = request.GET.get('category','')
    search = request.GET.get('search','')
    
    # 2.F함수사용 - filter검색후, 특정컬럼의 값을 가져오는 함수
    qs = Board.objects.filter(bno=bno) # 리스트
    qs.update(bhit = F('bhit')+1) #save까지 됨.
    context = {'board':qs[0],'category':category,'search':search}
    
    return render(request,'notice_read.html',context)

# 게시판리스트 (일반 게시판리스트, 검색 게시판리스트)
def list(request):
    # 현재 페이지
    page = int(request.GET.get('page',1)) # 없을때, 1페이지로 넘겨줌
    #search
    search = request.GET.get('search','') 
    category = request.GET.get('category','')
    print('검색데이터 : ',category,search)
    
    if search == '':  # 일반리스트로 넘어온 경우
        # 게시글 전체 가져오기
        qs = Board.objects.order_by('-bgroup','bstep')
        # 페이지 분기
        paginator = Paginator(qs,20) # 100개 -> 10개씩 쪼개서 전달해줌.
        list = paginator.get_page(page)  # 현재페이지에 해당되는 게시글 전달
        context = {"list":list,'page':page}
        return render(request,'notice_list.html',context)
    else:            
        # 검색으로 넘어온 경우
        # 게시글 전체 가져오기
        if category == 'btitle':
            qs = Board.objects.filter(btitle__contains=search)
        elif category == 'bcontent':
            qs = Board.objects.filter(bcontent__contains=search)
        elif category == 'all':
            qs = Board.objects.filter(Q(bcontent__contains=search) | Q(btitle__contains=search))

        # 페이지 분기
        paginator = Paginator(qs,20) # 100개 -> 10개씩 쪼개서 전달해줌.
        list = paginator.get_page(page)  # 현재페이지에 해당되는 게시글 전달
        context = {"list":list,'page':page, 'search':search, 'category':category}
        return render(request,'notice_list.html',context)

# def search(request):
#     if request.method == 'POST' :
#         category = request.POST.get('search')
#         keyword = request.POST.get('search')
#         if category == 'btitle':
#             q = Board.objects.filter(btitle__contains=keyword)
#         elif category == 'bcontent':
#             q = Board.objects.filter(bcontent__contains = keyword)
#         print(q)
#         return render(request, 'notice.list.html')

def update(request,bno):
    qs = Board.objects.get(bno=bno)
    if request.method == 'GET':
        context = {'board':qs}
        return render(request,'update.html',context)
    elif request.method == 'POST':
        id = request.POST.get('id')
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        bfile = request.POST.get('bfile')
        
        qs.id = id
        qs.btible = btitle
        qs.bcontent = bcontent
        qs.bfile = bfile
        qs.save()
        
        context = {'msg':1}
        return render(request,'update.html',context)

def delete(request, bno):
    Board.objects.get(bno=bno).delete()
    return redirect('/board/list/')

def reply(request, bno):
    qs = Board.objects.get(bno=bno)
    if request.method == 'GET':
        context = {'board':qs}
        return render(request,'reply.html',context)
    elif request.method == 'POST':
        id = request.POST.get('id')
        bgroup = request.POST.get('bgroup')
        bstep = int(request.POST.get('bstep'))
        bindent = int(request.POST.get('bindent'))
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        bfile = request.POST.get('bfile')
        
        # 모든 자식들은 전부 bstep을 1씩 증가시켜야 함
        # 부모보다 bstep 더 큰것은 전부 bstep 1씩 증가 gt,lt,gte,lte
        # F함수 현재 찾아진 컬럼의 값을 모두 가져옴
        reply_qs = Board.objects.filter(bgroup=bgroup, bstep__gt = bstep)
        reply_qs.update(bstep = F('bstep')+1) 
        # 2. DB 저장
        qs = Board.objects.create(id=id,btitle=btitle,bcontent=bcontent,bfile=bfile, bgroup=bgroup, bstep=bstep+1,bindent=bindent+1)
        
        context = {"msg":1, 'board':qs}
        
        return render(request,'reply.html',context)