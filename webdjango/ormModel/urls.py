from django.urls import path
from . import views
from . import views
urlpatterns = [
    path('orm/operate',views.index,name='operate'),
    path('orm/foreignKey',views.foreignKey, name="foreignKey"),
    path('orm/oneToMany',views.one_to_many_view, name="oneToMany"),
    path('orm/lookUp',views.loopUp, name="loopUp"),
    path('orm/aggregate',views.aggregate, name="aggregate")
]
#1 sql语句重复利用率不高
#2 很多sql语句是根据业务逻辑拼出来的,如果数据库需要更改，就要去修改
#3 写sql容易忽略web安全问题，给未来造成隐患 sql注入
#ORM 对象关系映射 通过ORM我们通过类来操作数据库，把表映射成类，把行映射成实例，把
#映射的命令:1.生成迁移脚本文件 python manage.py makemigrations
#映射的命令:2.使用生成的脚本进行映射 python manage.py migrate
#每张表都会有一个主键  Int类型,自增长，假如没有定义会自动帮我们定义
#如果你想一个对象打印得更加好看一点，那么可以重写__str__方法
#常用字段:AutoField BigAutoField BooleanField NullBoolField CharField TextField        UUIDField          URLField
#         int自增长 更多存储     布尔         布尔可空      不超过254 存储任意长度字符 32位全球唯一字符串 只能存储url格式
#         EmailField                                        FileField FloatField IntegerField BigIntegerField
#         在数据库层面并不会，只有在表单验证的时候会起作用  文件上传  浮点
#外键的使用 可以使得一张表可以引用另外一张表 自己引用自己的应用场景就是多级评论
#查询操作一般使用filter,exclude,get   field__condition
#聚合函数 avg

