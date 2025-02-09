from django.shortcuts import render, get_object_or_404 #웹 클라이언트에게 웹페이지 전달, 모델 클래스 안에 있는 객체 찾기
from django.http import HttpResponseRedirect            #리다이렉션을 위한 추가
from polls.models import Question, Choice                #Question 모델 클래스 추가
from django.urls import reverse                           #URLConf의 URL들중 별칭으로 URL 맵핑 
from . import forms                                        #from polls import forms (모델폼을 사용하기 위해 모듈추가)
from datetime import datetime                               #현재시간을 알기 위해 추가한 파이썬 기본 모듈 추가
# Create your views here.
#index.html 질문들
def index(request):
    #Question 테이블에 있는 모든 객체(데이터들)을 추출
    #order_by() 데이터를 정렬할 때 사용
    #a=[1,2,3,4,5] a[1:] -> [2,3,4,5]    a[:3] -> [1,2,3]
    latest_question_list = Question.objects.all().order_by('pub_date')[:5]
    #cotext 변수에 사전형으로 보낼 데이터 저장
    cotext = {'latest_question_list' : latest_question_list}
    #render 함수를 통해서 polls 폴더 안에 있는 index.html을 웹 클라이언트에게 전달 + HTML문서 변경에 사용할 cotext
    return render(request, 'polls/templates/index.html', context=cotext) #HttpResponse 객체를 반환함
#detail.html 질문 + 답변 페이지
def detail(request, question_id): #question_id = URL 표현식에서 가져온 값
    #Question 테이블에서 PK(기본키)rk question_id인 객체를 변환. 단, 없을경우 404 Error 반환
    question = get_object_or_404(Question,pk = question_id)
    return render(request, 'polls/templates/detail.html',{'question' : question})
    
#result.html 투표결과 보여주기
def results(request, question_id):
    question = get_object_or_404(Question,pk = question_id)
    return render(request, 'polls/templates/results.html',{'question' : question})

#투표 처리
def vote(request, question_id):
    p = get_object_or_404(Question,pk=question_id)
    #try~ catch ~ finally
    try:
        #get() 특정조건에 맞춰서 객체(데이터) 한개만 가져오는 함수
        selected = p.choice_set.get(pk=request.POST['choice'])
        
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/templates/detail.html',
                        {'question' : p, 'error_message' : "you didn't select a choice"})
    else:
        selected.votes += 1
        selected.save()
        return HttpResponseRedirect(reverse('results',args=(p.id,)))
    
def registerq(request):
    if request.method == 'GET': #사용자가 GET방식으로 요청 (웹페이지 접근)
        obj = forms.QuestionForm()  #QuestionForm 객체 생성 - HTML에서 <form>태그 안에 들어감
        return render(request, 'polls/templates/registerq.html',{'form' : obj})
    else:   #사용자가 POST방식으로 요청 (웹클라이언트가 웹서버에게 <form> 전달)
        obj = forms.QuestionForm(request.POST) #POST방식으로 온 데이터를 QuestionForm에 삽입
        if obj.is_valid():                      #사용자가 <Form>에 있는 양식을 잘 작성했는지 확인
            question = obj.save(commit = False) 
            #객체를 생성(DB에 반영 안 함) pub_date 속성에 값을 안 넣었기 때문에 save시 오류 발생
            question.pub_date=datetime.now()    #현재날짜를 pub_date 속성에 삽입
            question.save()                     #DB에 Question 객체 저장
            return HttpResponseRedirect( reverse('index') )
        else:
            #사용자가 입력한 값이 비정상적일때
            return render(request, 'polls/templates/registerq.html',{'form' : obj, 'error message' : '비정상적인 값입니다.'})

def registerc(request):
    if request.method == "GET":
        obj = forms.ChoiceForm()
        return render(request, 'polls/templates/registerc.html', {'form' : obj})
    else:
        obj = forms.ChoiceForm(request.POST)
        if obj.is_valid():
            choice = obj.save()
            return HttpResponseRedirect( reverse ('detail', args=(choice.question.id,) ) )
        else:
            return render(request, 'polls/templates/registerc.html',{'form' : obj})

def deleteQ(request,question_id):
    obj = get_object_or_404(Question, pk = question_id)
    obj.delete()
    return HttpResponseRedirect( reverse('index') )
    
def deleteC(request, choice_id):
    obj = get_object_or_404(Choice, pk = choice_id)
    obj.delete()
    return HttpResponseRedirect(reverse('index'))

def updateQ(request, question_id):
    obj = get_object_or_404(Question, pk = question_id)
    form = forms.QuestionForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('detail',args=(question_id)))
    return render(request, 'polls/templates/registerQ.html',{'form' : form})

def updateC(request, choice_id):
    obj = get_object_or_404(Choice, pk = choice_id)
    form = forms.ChoiceForm(request.POST or None, instance = obj)
    if form.is_valid():
        choice = form.save() #Choice 객체의 변경점을 저장
        #127.0.0.1:8000/polls/5/
        return HttpResponseRedirect(reverse('detail',args=(choice.question.id, )))
    return render(request, 'polls/templates/registerC.html',{'form' : form})
    
#질문의 제목으로 검색하는 기능(검색 기능은 GET방식)
def searchQ(request):
    q = request.GET.get('q','') #GET방식으로 접근했을 때 'q'라는 키값으로 저장된 값을 불러옴
    if q:
        qs = Question.objects.filter(question_text__contains = q) #질의 문(쿼리셋)
        
    return render(request, 'polls/templates/searchQ.html', { 'list' : qs, 'q' : q})

def searchC(request):
    q = request.GET.get('q',0)
    if q:
        qsC = Choice.objects.filter(votes__gte = int(q)).values("question") #객체의 votes값이 q보다 큰 객체를 검출
        qs = Question.objects.filter(id__in=qsC)    #qsC에 포함된 Choice객체와 연동된 Question 객체를 추출
    return render(request, 'polls/templates/searchC.html', { 'list' : qs, 'q' : q})

