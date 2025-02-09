'''
Created on 2018. 3. 31.

@author: admin
'''
from django.forms.models import ModelForm
from .models import Comment
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
        