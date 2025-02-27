'''
Created on 2018. 3. 24.

@author: admin
'''
from django.conf.urls import url
from . import views

app_name = 'blog' # 호출방법 {% url 'blog:index' %}
urlpatterns = [
    #127.0.0.1:8000/blog/
    #클래스 기반 뷰는 as_view()라는 함수를 써야 매칭이 가능
    url(r'^$',views.index.as_view(),name='index'), 
    url(r'^detail/(?P<pk>\d+)/$',views.detail.as_view(),name='detail'),
    url(r'^posting/$',views.posting.as_view(),name='posting'),
    url(r'^updateposting/(?P<pk>\d+)/$',views.updatePosting.as_view(),name='updateposting'),
    url(r'^comment/$',views.commentWrite, name='commentwrite'),
    url(r'^search/$',views.searchS,name='search'),
]