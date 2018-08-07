from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
# Create your views here.
def djangoRender(request):
    #内部也是用两条语句 render_to_responese这个也是快过期了
    return render(request, 'index.html')
    #html = render_to_string("index.html")
    #return HttpResponse(html)
class Company(object):
    def __init__(self,company):
        self.company = company
def djangoVariable(request):
    context = {
        'username':'oliver.he',
        'data':Company('MTK'),
        # 假如字典里面有一个key叫keys，这样子就返回keys对应的值，假如没有的话，就默认走python的语法，获取所有key
        'hobby':{
            'movie':'荒野求生'
        },
        'LOL':[
            "程咬金",
            "鲁班一号",
            "虞姬",
            "凯"
        ]
    }
    #context = "oliver.he" 这样写是错误的
    #值得注意的是，context必须是一个dir
    return render(request, 'variable.html',context = context)
def djangoTag(request,hero):
    context = {
        'hero':hero,
        'LOL': [
            "程咬金",
            "鲁班一号",
            "虞姬",
            "凯"
        ],
        'hobby': {
            'movie': '荒野求生',
            'music': 'love story',
            'programme':'python'
        },
        'book': [
            {'name':"三国演义","author":"罗贯中","price":99},
            {'name':"红楼梦","author":"曹雪芹","price":199},
            {'name':"西游记","author":"吴承恩","price":299},
            {'name':"水浒传","author":"施耐庵","price":399},
        ]
    }
    return render(request, 'tag.html', context = context)
def djangoDouban(request):
    return render(request, 'douban.html')
def djangoDouban_book(request):
    return HttpResponse("读书页面")
def djangoDouban_movie(request):
    return HttpResponse("电影页面")
def djangoDouban_go(request):
    return HttpResponse("同程页面")
def djangoDouban_book_detail(request,book_id):
    return HttpResponse("您的图书id是%s"%book_id)
def djangoDouban_login(request):
    next = request.GET.get('next')
    text = "您要跳转的页面是%s"%(next)
    return HttpResponse(text)
def djangoFilter(request):
    context = {
        'num1':50,
        'num2':'oliver.he'
    }
    return render(request, 'filter.html',context=context)
def greet():
    return "hello"
def djangoInherit(request):
    context = {
        'username':'oliver.he'
    }
    return render(request, 'inherit_index.html',context=context)
def djangoInheritCompany(request):
    context = {
        'username':'oliver.he'
    }
    return render(request, 'inherit_company.html',context=context)
def djangoInheritSchool(request):
    context = {
        'username':'oliver.he'
    }
    return render(request, 'inherit_school.html',context=context)
def djangoLoadStatic(request):
    return render(request, 'loadStatic.html')