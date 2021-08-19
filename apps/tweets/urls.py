from django.urls import path

from . import views

app_name = "tweets"

urlpatterns = [
    path('index', views.index, name='index'),
    path('test', views.test, name='test'),
]
