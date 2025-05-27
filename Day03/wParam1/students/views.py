from django.shortcuts import render

# Create your views here.

def result(request):
    name = request.GET.get('name')
    id = request.GET.get('id')
    pw = request.GET.get('pw')
    context = {'name':name, 'id':id, 'pw':pw}
    return render(request, 'result.html',context)