from . import views
from django.urls import path

urlpatterns = [
    path('', views.home),
    path(r'init/',views.init),
    path(r'getShader/',views.getShader),
    path(r'gethd/',views.gethd),
    path(r'getdd/',views.getdd),
    path(r'getsl/',views.getsl),
]