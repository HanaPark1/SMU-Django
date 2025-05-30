from django.shortcuts import render

# Create your views here.

def list(request):
    return render(request, 'notice_list.html')

def read(request):
    return render(request, 'notice_read.html')

def write(request):
    return render(request, 'write.html')