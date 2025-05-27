from django.urls import path
from . import views

app_name = 'students'
urlpatterns = [
    path('list/', views.list, name="list"),
    path('view/', views.view, name="view"),
    path('write/', views.write, name='write'),
    path('result/', views.result, name='result'),
    path('send/<str:name>/<int:age>/', views.send, name='send'),
]
