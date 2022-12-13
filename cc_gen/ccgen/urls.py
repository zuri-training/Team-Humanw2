from django.urls import path
from . import views

app_name="ccgen"
urlpatterns=[
    path('signup/', views.userCreateview.as_view(), name='usersignup'),
]
