
from django.urls import path
from . import views

app_name = 'member'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('step01/', views.step01, name='step01'),
]
