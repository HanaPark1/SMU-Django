from django.shortcuts import render

# Create your views here.

def list(request):
    id = request.POST.get('id')
    pw = request.POST.get('pw')
    gender = request.POST.get('gender')
    tel = request.POST.get('tel')
    context = {"id":id, "pw":pw, "gender":gender,'tel':tel}
    return render(request, 'list.html', context)