
from django.urls import path
from testapp import views
from rest_framework.routers import SimpleRouter


# 创建一个一个Simplerouter对象
# routers = SimpleRouter()
# 注册获取数据的API接口路由，执行的视图为'views.showallstu'
# routers.register(r'book', views.getbook.as_view({'get': 'list'}), base_name='')
urlpatterns = [
    path('test/',views.test),
    # path('test2/',views.test2),
    path('test2/',views.paginator_view),
    path(r'book/',views.getlist),
    path(r'search/',views.bookcha),
]
# 将注册路由添加到django路由系统中
# urlpatterns += routers.urls