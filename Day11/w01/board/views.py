from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def list(request):
    return render(request, 'list.html')

#form 전송방식
def view(request):
    if request.method == 'GET':
        return render(request, 'view.html')
    elif request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        
        context = {'id':id, 'name':name}
        return render(request, 'view.html', context)
        
# ajax 전송방식
def view2(request):
    id = request.POST.get('id', '')
    name = request.POST.get('name', '')
    
    # JSON 응답을 반환
    context = {
        'id': id,
        'name': name,
        'pw': '1111',
        'success': 'success'
    }
    return JsonResponse(context)  # ← 반드시 return 해야 함
