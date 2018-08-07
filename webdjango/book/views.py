from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect,reverse
from django.template.loader import render_to_string
# Create your views here.
def detail(request,book_detail):
    #ip对应http://127.0.0.1:8000/book/detail/asdsada1
    #也可以传多个
    test = ("book id is:%s"%book_detail)
    return HttpResponse(test)
def id(request):
    author_detail = request.GET.get('id')
    author_detail = request.GET['id']
    #http://192.168.1.100:8000/book/id/?id=2
    text = HttpResponse("id is:%s"%author_detail)
    return text
def main(request):
    if request.GET.get('username'):
        return HttpResponse("主页")
    else:
        return redirect(reverse('book:login'))
def login(request):
    return HttpResponse("登录页面")
