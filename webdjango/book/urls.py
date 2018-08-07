from django.urls import path
from . import views
#应用命名空间
app_name = 'book'
urlpatterns = [
    path('book/detail/<book_detail>/',views.detail, name='detail'),
    path('book/id/',views.id, name='id'),
    path('book/main/',views.main, name='main'),
    path('book/login/',views.login, name='login')
    #拓展:假如其他app也有login这个url name，那应该怎么办呢，这个时候我们可以通过命名空间解决这个问题


]
#app主要演示如何使用url name,url传参，跳转到其他url，以及反转url,命名空间