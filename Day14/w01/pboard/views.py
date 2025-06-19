from django.shortcuts import render
import requests
import json

### 전역변수
dlist = []

# 공공데이터 상세보기 - 공공데이터 다시 호출
def view(request,galContentId):
    global dlist
    print('넘어온 galContentId : ',galContentId)
    print('넘어온 dlist : ',dlist)
    # 공공데이터 호출
    # dlist = publicData()
    for d in dlist:
        if d['galContentId'] == str(galContentId): # 타입확인
            dData = d
            break
        
    context = {'dData':dData}
    return render(request,'pboard/view.html',context)


# 공공데이터 리스트
def list(request):
    global dlist
    dlist = publicData()
    context = {'list':dlist}
    return render(request,'pboard/list.html',context)

# 공공데이터 가져오기 함수    
def publicData():
    public_key = '%2FkR9HCv6YxY%2BIeqWi9UvUKEJOq%2BLYqmmG13nKO1%2BxTsnOnFq0Kfd4%2BwlGPwquoCQRfOXb14SqKhKucCRsv%2BeOw%3D%3D'
    pageNo = 1
    url = f'http://apis.data.go.kr/B551011/PhotoGalleryService1/galleryList1?serviceKey={public_key}&numOfRows=10&pageNo={pageNo}&MobileOS=ETC&MobileApp=AppTest&arrange=A&_type=json'
    # 웹스크래핑 requests
    response = requests.get(url)
    #print("공공데이터 : ",response.text)  # str타입
    
    # 문자열 -> json타입으로 변경
    json_data = json.loads(response.text)
    dlist = json_data['response']['body']['items']['item']
    # print('json데이터 : ',json_data['response']['body']['items']['item'])     # json타입
    # print('json데이터 1개 : ',json_data['response']['body']['items']['item'][0])
    
    return dlist    