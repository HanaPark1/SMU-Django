from django.shortcuts import render

# 차트페이지 호출
def chlist(request):
    profit = [12, 19, 3, 5, 2, 3]
    context = {'profit':profit}
    return render(request,'chart/chlist.html',context)
