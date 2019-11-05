
import json
import status as status
from django.core.paginator import Paginator, PageNotAnInteger, InvalidPage, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import mixins, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from testapp import models
# Create your views here.
from testapp.serializers import MeiziSerializer


def test(request):
    test=models.book_zhoudu.objects.filter(name__in=["书名：捐赠","书名：南方高速"]).all()
    print(test)
    return render(request,r'testapp\test.html',{'test1':test})


def bookcha(request):
    book_id=request.GET['id']
    print(type(book_id))
    book_info = models.book_zhoudu.objects.filter(id=book_id).values('id', 'name', 'author', 'fenlei', 'score','dwlink1','dwlink2','dwlink3')
    print(type(book_info))
    # book_info=models.book_zhoudu.objects.all()[0:21]
    # print(test)
    # return render(request,r'testapp\test1.html',{'book':book_info})
    res=json.dumps(list(book_info))
    # data=json.loads('''[{"id": 2, "name": "\u4e66\u540d\uff1a\u8ba9\u53f6\u5170\u7ee7\u7eed\u98d8\u626c", "author": "\u4f5c\u8005\uff1a\u6cbb\u00b7\u5965\u5a01\u5c14", "fenlei": "\u5206\u7c7b\uff1a\u5916\u56fd\u6587\u5b66", "score": "\u8c46\u74e3\u8bc4\u5206\uff1a8.8", "dwlink1": "https://pan.baidu.com/s/1zVmfZYFYrmXfCUX0zjtC6A", "dwlink2": "https://share.weiyun.com/559oC2g", "dwlink3": "https://tc5.us/dir/18798378-35422641-87c67d"}]''',encoding='utf-8')
    return HttpResponse(json.loads(res,encoding='utf-8'))
    # print(data)
    # return HttpResponse(data)

def print_base_dir(request):
    pass

# #向表内添加数据
# from django.http import HttpResponse
# from .models import Goods
# import random
# # Create your views here.
#
# def index(request):
#     for x in range(200):
#         good = Goods(name='good%s'%x,des='该商品物美价廉，现在只需要{}元'.format(random.randint(10,100)))
#         good.save()
#     return  HttpResponse('数据添加成功')


def paginator_view(request):
    book_list = models.book_zhoudu.objects.all()
    # 将数据按照规定每页显示 20 条, 进行分割
    paginator = Paginator(book_list, 20)

    if request.method == "GET":
        # 获取 url 后面的 page 参数的值, 首页不显示 page 参数, 默认值是 1
        page = request.GET.get('page')
        try:
            books = paginator.page(page)
        # todo: 注意捕获异常
        except PageNotAnInteger:
            # 如果请求的页数不是整数, 返回第一页。
            books = paginator.page(1)
        except InvalidPage:
            # 如果请求的页数不存在, 重定向页面
            return HttpResponse('找不到页面的内容')
        except EmptyPage:
            # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
            books = paginator.page(paginator.num_pages)

    template_view = 'testapp\page.html'
    return render(request, template_view, {'books': books})


@api_view(['GET', 'POST'])
def getlist(request, format=None):
    if request.method == 'GET':
        meizis = models.book_zhoudu.objects.all()[0:10]
        serializer = MeiziSerializer(meizis,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MeiziSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


