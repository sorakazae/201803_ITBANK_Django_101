from django.db import models
from unittest.util import _MAX_LENGTH

# Create your models here.

#Question 테이블 생성
#models.Model : 모델 클래스를 만들 때 필요한 관련 메소드를 저장
class Question(models.Model):
    #id
    #choice        Choice에서 참조해서 역참조도 가능
    question_text = models.CharField(max_length=200) #models.CharField -> 테이블에 글자를 저장할 때 사용
    pub_date = models.DateTimeField('date published') #models.DateTimeField -> 테이블에 날짜시간을 저장할때 사용
    def __str__(self):
        return self.question_text
    
#Choice 테이블 생성
#Choice_text 글자 200자, votes 숫자 models.IntegerField
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #외래키 설정, 해당하는 테이블의 Primary Key를 참조 => Question.id
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    
class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()
    
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    
    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()
    
    def __str__(self):
        return self.headline
    