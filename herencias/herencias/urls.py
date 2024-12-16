
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('herencias/', views.herencias, name='herencias'),
    path('ejemploh/', views.ejemploh, name='ejemploh'),
    path('otrah/', views.otrah, name='otrah'),
    path('', views.index, name='index'),
    
]
