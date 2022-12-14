from django.urls import path
from . import views

app_name="ccgen"
urlpatterns=[
<<<<<<< HEAD
    path('', views.index, name='index'),
  
=======
>>>>>>> khun
    path('signup/', views.userCreateview.as_view(), name='usersignup'),
]
