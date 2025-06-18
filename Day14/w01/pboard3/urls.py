from django.urls import path,include
from . import views

app_name='pboard3'
urlpatterns = [
    path('list/', views.list, name='list'),
    path('view/<int:movieCd>/', views.view, name='view'),
]
