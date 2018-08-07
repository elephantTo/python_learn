from django.shortcuts import render
from django.db import connection
#
# # Create your views here.
def connectMysql(request):
    cursor = connection.cursor()
    cursor.execute("insert into book(id,name,author) value(null,'水浒传','施耐庵')")
    cursor.execute("select * from book")
    rows = cursor.fetchall()
    return render(request, 'index.html')