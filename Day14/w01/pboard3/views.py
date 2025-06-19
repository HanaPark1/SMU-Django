from django.shortcuts import render
from django.http import JsonResponse
import requests
import json

### 전역변수
dlist = [] # list함수에서 공공데이터를 가지고 와서 view 함수에 전달

# Create your views here.

def list(request):
    global dlist
    # 데이터 가져올 정보
    targetDt = 20250617
    dlist = publicScreen(targetDt)
    context = {'list':dlist}
    
    return render(request, 'pboard3/list.html', context)

def view(request, movieCd):
    global dlist
    context = {}
    for m in dlist:
        if( m['movieCd'] == str(movieCd)):
            context['mData'] = m
            
    print('mData: ', context['mData'])
    return render(request, 'pboard3/view.html', context)

# ajax통신 - 리턴타입 JsonResponse
def searchAjax(request) :
    global dlist
    
    targetDt = request.POST.get('searchInput','20250617')
    
    dlist = publicScreen(targetDt)
    
    context = {'list':dlist}
    
    return JsonResponse(context)

def publicScreen(targetDt):
    global dlist
    
    targetDt = targetDt
    key = '9289e94e12ce8b0192036deed058b0c9'
    url = f'http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key={key}&targetDt={targetDt}'
    
    response = requests.get(url)
    json_data = json.loads(response.text)
    
    dlist = json_data['boxOfficeResult']['dailyBoxOfficeList']
    return dlist