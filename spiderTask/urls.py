from django.conf.urls import url

from spiderTask import views

urlpatterns = [
    # 测试跑通
    url(r'index', views.index, name='index'),

]