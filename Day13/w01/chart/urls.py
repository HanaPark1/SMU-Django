from django.urls import path,include
from . import views

app_name='chart/'
urlpatterns = [
    path('chlist/', views.chlist, name='chlist'),
    path('chajax/', views.chajax, name='chajax'),
    path('chlist2/', views.chlist2, name='chlist2'),
    path('chlist3/', views.chlist3, name='chlist3'),
    path('chajax2/', views.chajax2, name='chajax2'),

]