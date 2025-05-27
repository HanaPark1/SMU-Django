from django.urls import path
from . import views

app_name = ''
urlpatterns = [
    path('result/<int:id>/<int:pw>/<str:name>', views.result, name='result'),
]
