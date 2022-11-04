from django.urls import path
from myapp import views
urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    path('read/<id>/', views.read),
    path('update/<id>/', views.update),
    path('delete/', views.delete)
    
]
   
#사용자가 경로를 지정하지 않았을 때 ' ' 인덱스로 위임하려면
# 공백의 경로로 들어왔을 때 views.index가 실행이 될 것이다. 

