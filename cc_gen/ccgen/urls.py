from django.urls import path
from . import views

app_name="ccgen"
urlpatterns=[

    path('', views.index, name='index'),
    path('alldesigns/', views.designListView.as_view(), name='designs'),
    path('design/<int:pk>', views.designDetailView.as_view(), name='design-detail'),
    path('design/create/', views.designCreate.as_view(),name='design-create'),
    path('design/<int:pk>/delete/', views.designDelete.as_view(), name='design-delete'),   
    path('downloads/', views.downloadedListView.as_view(), name='downloads'),
    path('saveddownloads/', views.savedfordownloadListView.as_view(), name='saved'),
    path('update-download-field/', views.update_download_field, name='update-download-field'),

    path('signup/', views.userCreateview.as_view(), name='usersignup'),
]
