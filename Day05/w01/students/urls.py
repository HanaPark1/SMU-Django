from django.urls import path
from . import views

app_name = 'students'
urlpatterns = [
    path('list/', views.list, name='list'),
    path('write/', views.write, name='write'),
    path('view/<int:no>/', views.view, name='view'),
    path('update/<int:no>/', views.update, name='update'),
    path('delete/<int:no>/', views.delete, name='delete'),
]
