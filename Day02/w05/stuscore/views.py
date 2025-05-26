from django.shortcuts import render
from stuscore.models import Stuscore

# Create your views here.

def result(request):
    qs = Stuscore.objects.all()
    context = {'list':qs}
    return render(request, 'result.html',context)