from django.db import models
from django.conf import settings
# Create your models here.
class Boardtype(models.Model):
    name = models.CharField('구분',max_length=100)
    #post
    def __str__(self):
        return self.name
    
class Board(models.Model):
    type = models.ForeignKey(Boardtype,on_delete=models.CASCADE)
    headline = models.CharField('제목',max_length=200)
    content = models.TextField('내용',null=True,blank=True)
    pub_date = models.DateField('날짜',auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True,null=True)
    #files
    
class File(models.Model):
    board = models.ForeignKey(Board,on_delete=models.CASCADE)
    files = models.FileField('파일',upload_to='uploads/<author>/%Y%m%d/content/')
    
class Money(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    point = models.IntegerField('포인트')
    
class Comment(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    comment = models.TextField('댓글')
    def __str__(self):
        return self.comment
