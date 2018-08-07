from django.shortcuts import render
from django.db import models
from .models import Book,Category,Article,agg_Publisher,agg_Author,agg_Book,agg_BookOrder
from djangoTemplate.models import FrontUser
from django.http import HttpResponse
from django.db.models import Avg
from django.db import connection
# Create your views here.
def index(request):
    # # 1.使用ORM添加一条数据到数据库中
    # book = Book(name="三国演义",author="罗贯中",price=200)
    # book.save()

    #2. 查询
    #根据主键进行查找
    book = Book.objects.get(pk=1)
    print(book)
    #根据其他条件查找
    book = Book.objects.filter(name="三国演义")
    book_first = Book.objects.filter(name="三国演义").first()
    print(book)

    #3. 删除
    book = Book.objects.get(pk=0)
    book.delete()

    #4. 修改
    book = Book.objects.get(pk=2)
    book.price = 100
    book.save()
    return HttpResponse("书籍修改成功")
def foreignKey(request):
    article = Article(title='abc',content='111')
    category = Category(name='最新文章')
    category.save()
    article.category = category
    article.save()
    # article = Article.objects.first()
    # print(article.category.name)
    #如果想引用其他App里面models 就用app.model
    return HttpResponse("foreignKey success")
def one_to_many_view(request):
    #一对多的关联操作
    # article = Article(title="钢铁是怎样炼成的")
    # category = Category.objects.first()
    # author = FrontUser.objects.first()
    #
    # article.category = category
    # article.author = author
    # article.save()
    #获取分类下所有的文章
    category = Category.objects.first()
    #relatedManager  article_set会没有加入定义了releated_name
    #article = category.article_set.all()
    article = category.articles.all()
    print(article)
    article = Article(title="追风筝的人")
    article.author = FrontUser.objects.first()
    #假如定义了bulk，就可以执行article.save()
    #article.save()
    category.articles.add(article,bluk=False)
    category.save()
    return HttpResponse("一对多")
def loopUp(request):
    #对大小写不敏感 linuxSystem可以编辑数据库设置排序规则为utf8_bin，这样子可以大小写敏感  但windows下设置没有用，因为window用的是unicode
    article = Article.objects.filter(title__iexact='追风筝的人')
    print(article)
    article = Article.objects.filter(title__icontains="追")
    print(article)
    #如下打印可以知道对应翻译成什么mysql语句
    #仅限于filter
    print(type(article))
    print(article.query)
    return HttpResponse("查询操作")
def aggregate(request):
    #获取图书定价的平均价 avg是自己命名的别名  也可以不写Avg=
    result = agg_Book.objects.aggregate(avg=Avg("price"))
    print(result)
    #only querySet can use
    #print(result.query)
    print(connection.queries)
    return HttpResponse()
