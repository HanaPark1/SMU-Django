
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'customer'
urlpatterns = [
    path('list/', views.list, name='list'),
    path('view/<int:bno>/', views.view, name='view'),
    path('write/', views.write, name='write'),
]

# 파일업로드시 url구성 , urlpatterns 에 추가로 설정이 들어감.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)