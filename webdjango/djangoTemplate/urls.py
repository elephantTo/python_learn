from django.urls import path
from . import views
urlpatterns = [
    path('template/render',views.djangoRender, name='render'),
    path('template/variable',views.djangoVariable, name='variable'),
    path('template/tag/<hero>',views.djangoTag, name='tag'),
    path('template/douban/',views.djangoDouban, name='douban'),
    path('template/douban/book',views.djangoDouban_book, name='douban_book'),
    path('template/douban/movie',views.djangoDouban_movie, name='douban_movie'),
    path('template/douban/go',views.djangoDouban_go, name='douban_go'),
    path('template/douban/book/detail/<book_id>',views.djangoDouban_book_detail, name='douban_book_detail'),
    path('template/douban/login',views.djangoDouban_login, name='douban_login'),
    path('template/filter',views.djangoFilter, name='filter'),
    path('template/inherit',views.djangoInherit, name='inherit'),
    path('template/inherit/company',views.djangoInheritCompany, name='inherit_company'),
    path('template/inherit/school',views.djangoInheritSchool, name='inherit_school'),
    path('template/loadStatic',views.djangoLoadStatic, name='loadStatic')
]
#app演示
# 如何渲染html,背景粉红色：djangoRender
#模板查找顺序DIRS->APP_DIRS(必须在install app写上自己的app才能搜索到)
#模板变量:djangoVariable
#所有的标签都在{% %}
#模板标签:djangoTag
#模板里面的url跳转，以及传参:djangoDouabn
#模板可以调用函数，但是并不能调用函数传参，有很大的局限性,这样导致数据处理没办法通过函数完成，这个时候就要用到过滤器，更多过滤器请参考https://blog.csdn.net/foryouslgme/article/details/52057445
#模板过滤器:djangoFilter
#模板继承:djangoInherit
#模板加载静态文件:djangoLoadStatic  css/js/图片
#表关系一对多:文章和作者之间的关系
