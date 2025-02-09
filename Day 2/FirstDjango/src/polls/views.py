from django.shortcuts import render, get_object_or_404 #웹 클라이언트에게 웹페이지 전달, 모델 클래스 안에 있는 객체 찾기
from django.http import HttpResponseRedirect #리다이렉션을 위한 추가
from polls.models import Question, Choice #Question 모델 클래스 추가
from django.urls import reverse #URLConf의 URL들중 별칭으로 URL 맵핑 
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
