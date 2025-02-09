from django.shortcuts import render
from .models import Post, Posttype, Image, Comment
# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy
from django.urls import reverse
from .forms import CommentForm
'''
def index(request):
    obj = Post.objects.all()[:10]
    return render(request, 'blog/templates/index.html',{'post' : obj})
'''

class index(ListView):
    template_name = 'blog/templates/index.html' #매칭할 템플릿 경로
    model = Post    #사용할 모델 클래스 설정
    paginate_by = 2 #한페이지에 몇개의 객체를 보여줄 것인지 설정
    context_object_name = 'post' #템플릿에 모델 객체들을 넘겨줄때 사용할 변수 이름
    #def get_queryset(self):
    #    return ListView.get_queryset(self)
    
class detail(DetailView):
    template_name = 'blog/templates/detail.html'
    model = Post
    context_object_name = 'post'
    def get_context_data(self, **kwargs): #템플릿 엔진에서 사용할 수 있도록 키:값 매칭해주는 메소드
        #DetailView에 있는 get_context_data 메소드를 사용해 기존에 셋팅해야되는 변수값들을 설정
        obj = DetailView.get_context_data(self, **kwargs)
        obj['form'] = CommentForm() #form 변수에 CommentForm 전달
        #=> render(request,'',{'form':CommentForm()})
        return obj
class posting(LoginRequiredMixin, CreateView):
    model = Post
    fields=['type','headline','content',]
    #success_url = reverse_lazy('blog:index')# url 셋팅이 완료된 후에 reverse를 하겠다는 의미(class로 구현해서)
    template_name = 'blog/templates/posting.html'
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user 
        obj.save()
        for f in self.request.FILES.getlist('files'):
            image = Image(post=obj,image=f)
            image.save()
        #success_url을 쓰지 않고 괄호 안에 reverse로 해도 됨
        #return HttpResponseRedirect(self.success_url) 
        return HttpResponseRedirect(reverse('blog:index',args=(obj.id,)))
    
class updatePosting(LoginRequiredMixin,UpdateView):
    model = Post
    fields = ['type','headline','content']
    template_name = 'blog/templates/updateposting.html'
    success_url = reverse_lazy('blog:index')
     
def commentWrite(request):
    if request.method == "POST":
        obj = Post.objects.get(id = request.POST['postid'])
        com = Comment(post = obj, comment = request.POST['comment'])
        com.save()
        return HttpResponseRedirect(reverse('blog:detail',args=(request.POST['postid'])))
    else:
        return HttpResponseRedirect(reverse('blog:index'))
#함수 기반으로 구현
def searchS(request):
    s = request.GET.get('name','')
    c = request.GET.get('sel','')
    if c=='1':
        ss = Post.objects.filter(headline__contains = s)
    elif c=='2':
        ss = Post.objects.filter(content__contains = s)
        
    return render(request, 'blog/templates/search.html',{'list':ss,'s':s,'c':c})

'''  클래스 기반으로 구현
class searchS(ListView):
    template_name = 'blog/templates/search.html'
    model = Post()
    paginate_by = 10
    context_object_name = 'post'
    def get_queryset(self):
        try:
            #GET타입으로 온 데이터 중 'name', 'sel' 변수 값을 읽음
            name=self.request.GET['name']
            sel = self.request.GET['sel']
        except:
            #읽는 중에 오류가 발생(실제값이 없을 때)하면 기본값 설정
            name=''
            sel='1'
        #제목으로 검색했는지 내용으로 검색했는지 비교
        if sel=='1':
            #Post의 headline 속성에 값으로 객체 추출
            #self.model -> model 속성에 지정한 Post 클래스
            object_list = self.model.objects.filter(headline_contains=name)
        elif sel == '2':
            #Post의 content 속성에 값으로 객체 추출
            object_list = self.model.objects.filter(content_contains=name)
            
        return object_list
'''