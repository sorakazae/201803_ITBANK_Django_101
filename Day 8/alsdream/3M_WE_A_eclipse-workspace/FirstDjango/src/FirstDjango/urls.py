"""FirstDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url #url 정규식을 구현하기 위해서 포함
from polls import views         # view 함수, 클래스 구현을 한 파일을 추가

from django.urls.conf import include    #다른 urls.py를 포함할때 사용하는 함수

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^polls/$', views.index ,name='index'), #URL 등록 127.0.0.1:8000/polls/
    #127.0.0.1:8000/polls/10/ -> question_id = 10
    url(r'^polls/(?P<question_id>\d+)/$', views.detail,name='detail'), #(?p) : 내가 정규표현식을 쓴다고 선언, <>는 변수 명
    #127.0.0.1:8000/polls/10/vote
    url(r'^polls/(?P<question_id>\d+)/vote/$', views.vote ,name='vote'),
    
    url(r'^polls/(?P<question_id>\d+)/results/$', views.results ,name='results'),
    
    #127.0.0.1:8000/polls/registerq/
    url(r'^polls/registerq/$', views.registerq, name='registerq'),
    url(r'^polls/registerc/$', views.registerc, name='registerc'),
    
    #127.0.0.1:8000/polls/delete/$
    url(r'^polls/deleteQ/(?P<question_id>\d+)/$',views.deleteQ, name = 'deleteQ'),
    url(r'^polls/deleteC/(?P<choice_id>\d+)/$',views.deleteC, name = 'deleteC'),
    
    url(r'^polls/updateQ/(?P<question_id>\d+)/$',views.updateQ,name = 'updateQ'),
    url(r'^polls/updateC/(?P<choice_id>\d+)/$',views.updateC,name = 'updateC'),
    
    #127.0.0.1:8000/polls/search?q='asdf'
    url(r'^polls/searchQ/$',views.searchQ, name = 'searchQ'),
    url(r'^polls/searchC/$',views.searchC, name = 'searchC'),
    
    #127.0.0.1:8000/user 주소를 전부 user.urls.py 처리
    #url(r'^user/',include('user.urls')),    # 처리를 user에 있는 urls.py에 넘김
    url(r'^user/', include('user.urls')),
    url(r'^auth/',include('social_django.urls')), #OAuth2.0 URL 추가
    # social:내부의 별칭
    
    url(r'^blog/',include('blog.urls')),
    
]
#정적인 미디어파일을 URL로 매칭
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)