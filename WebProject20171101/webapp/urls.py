#-*-coding:utf-8-*-
from django.conf.urls import url
from  webapp import views

urlpatterns = [
    #注册逻辑
    url(r'^register/$', views.register),
    #登陆创建登陆首页
    url(r'^login/$', views.login),
    #登陆人中逻辑
    url(r'^login_check/$', views.login_check),
    #个人主页
    url(r'^$', views.home,name='blog_home'),
    #程序主页
    url(r'^index/$', views.index,name='tablist'),
    #退出逻辑
    url(r'^logout/$', views.logout),
    url(r'^post/(?P<id>\d+)/$',views.Detail,name="blog_detail"),

]