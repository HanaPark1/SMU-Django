from django.shortcuts import render
from customer.models import Customer
from django.core.paginator import Paginator

# Create your views here.

def list(request):
    #요청하는 page 번호 가져오기 str->int
    page = int(request.GET.get('page',1))
    
    qs = Customer.objects.all().order_by('-ntchk', '-bgroup', 'bstep')
    # 10개 단위로 qs 분리
    paginator = Paginator(qs,10)
    
    # 가져올 페이지 선택
    customerList = paginator.get_page(page)
    print('-------------')
    print(customerList)
    print('-------------')
    
    # 게시글 10개, 현재 페이지 보냄
    context = {'list':customerList, 'page':page}
    return render(request, 'customer/list.html', context)

def view(request, bno):
    return render(request, 'customer/view.html')

def write(request):
    if request.method == 'GET':
        return render(request, 'customer/write.html')
    elif request.method == 'POST':
        return render(request, 'customer/write.html')