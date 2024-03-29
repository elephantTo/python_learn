from django.shortcuts import render,redirect,reverse
from django.db import connection
# Create your views here.
def get_corsor():
    return connection.cursor()
def index(request):
    cursor = get_corsor()
    cursor.execute("select id,name,author from book")
    books=cursor.fetchall()
    #[(1,'三国演义,'罗贯中')，（）]
    return render(request,'index.html',context={"books":books})
def addBook(request):
    if request.method == "GET":
        return render(request,'addBook.html')
    else:
        name = request.POST.get("name")
        author = request.POST.get("author")
        cursor = get_corsor()
        cursor.execute("insert into book(id,name,author) values(null,'%s','%s')"%(name,author))
        #会报CSRF错误
    return redirect(reverse("index"))
def bookDetail(request,book_id):
    cursor = get_corsor()
    cursor.execute("select id,name,author from book where id=%s"%book_id)
    book = cursor.fetchone()
    return render(request, 'bookDetail.html',context={"book":book})
def deleteBook(request):
    if request.method == "POST":
        book_id = request.POST.get("book_id")
        cursor = get_corsor()
        cursor.execute("delete from book where id=%s"%book_id)
        return redirect(reverse("index"))
    else:
        print("oliver.he")
        print(request.method)
        raise RuntimeError("删除图书的method错误")

