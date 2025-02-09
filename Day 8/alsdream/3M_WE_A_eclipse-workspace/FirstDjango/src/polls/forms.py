'''
Created on 2018. 3. 17.

@author: admin
'''

from django.forms.models import ModelForm #모델에 관련된 HTML폼을 작성할 때 사용
from . import models
class QuestionForm(ModelForm):
    class Meta:
        #model : 내가 연결할 모델 클래스
        #fields : 모델 속성중 사용자가 작성해야하는 것을 명시
        #exclude : 명시한 속성을 제외한 속성을 사용자가 작성해야 함
        model = models.Question
        fields = ['question_text',]
        
class ChoiceForm(ModelForm):
    class Meta:
        model = models.Choice
        exclude = ['votes',]
        
        
        
        
        
