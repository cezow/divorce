from django.urls import path
from divorcepoll import views

urlpatterns = [
    path('', views.index),
    path('result', views.result, name='result'),
]