from django.db import models

#如果要将一个普通的类变成一个可以映射成数据库中的ORM模型
class Book(models.Model):
    #id int 自增长
    key = models.AutoField(primary_key=True)
    #name varchar(100)
    name = models.CharField(max_length=100,null=False)
    #author varchar(100)
    author =  models.CharField(max_length=100,null=False)
    #price float
    price = models.FloatField(null=False,default=0)
    def __str__(self):
        return "<book:({name},{author},{price})>".format(name=self.name,author=self.author,price=self.price)
#一对多
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    #后面的形参表示两个表之间的关系 例如级联删除 引用的表来影响当前的表
    # category = models.ForeignKey("Category",on_delete=models.CASCADE,related_name = 'articles',null=True)
    # author = models.ForeignKey("djangoTemplate.FrontUser",on_delete=models.CASCADE,null=True)
    def __str__(self):
        # return "<article:({title},{content},{category})>".format(title=self.title,content=self.content,category=self.category,author=self.author)
        return "<article:({title},{content})>".format(title=self.title,content=self.content)
class Category(models.Model):
    name = models.CharField(max_length=100)
class Comment(models.Model):
    content = models.TextField()
    origin_comment = models.ForeignKey("self",on_delete=models.CASCADE)
#聚合模型
class agg_Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    class agg_Meta:
        db_table = 'author'
class agg_Publisher(models.Model):
    name = models.CharField(max_length=300)
    class agg_Meta:
        db_table = 'publisher'
class agg_Book(models.Model):
    name = models.CharField(max_length=300)
    page = models.IntegerField()
    price = models.FloatField()
    rating = models.FloatField()
    author = models.ForeignKey(agg_Author,on_delete=models.CASCADE)
    publisher = models.ForeignKey(agg_Publisher,on_delete=models.CASCADE)
    class agg_Meta:
        db_table = 'book'
class agg_BookOrder(models.Model):
    book = models.ForeignKey("book",on_delete=models.CASCADE)
    price = models.FloatField()
    class agg_Meta:
        db_table = 'bookOrder'



