from django.urls import path
from . import views

app_name="ccgen"
urlpatterns=[
    path('', views.index, name='index'),
  
]
