from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def list(request):
    return HttpResponse('페이지가 열립니다')
    # return render(request,'list.html')