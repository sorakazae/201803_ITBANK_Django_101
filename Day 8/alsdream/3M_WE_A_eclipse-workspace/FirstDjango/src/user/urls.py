'''
Created on 2018. 3. 24.

@author: admin
'''
from django.conf.urls import url
from django.contrib.auth.views import login, logout
from . import views # from user import views

app_name = 'user'   #{% url 'user:sign' %} // user에 있는 sign
urlpatterns = [
    url(r'^sign/',views.sign,name='sign'),     #회원 가입
    #url(r'^login/',login,name='login'),   #장고 기본제공 로그인 뷰 registration/login.html
    #url(r'^logout/',logout,name='logout'), #장고 기본제공 로그아웃 뷰
    url(r'^login/$',views.clogin,name='login'),
    url(r'^logout/$',views.clogout,name='logout'),
    
]