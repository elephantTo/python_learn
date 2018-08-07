from django.urls import path
from . import views
urlpatterns = [
    path('connectMysql',views.connectMysql, name='connectMysql')
]
#app演示如何简单操作mysql
