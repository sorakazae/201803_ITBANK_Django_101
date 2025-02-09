from django.db import models
from django.conf import settings
# Create your models here.
class Posttype(models.Model):
    name = models.CharField('구분',max_length=100)
    #post
    def __str__(self):
        return self.name
    
    
class Post(models.Model):
    type = models.ForeignKey(Posttype,on_delete=models.CASCADE) #CASCADE = 연관된 모든것을 같이 지우겠다
    headline = models.CharField('제목',max_length=200)
    #image
    #comment
    #null : DB내에 빈칸(NULL)으로 존재하고자 할 때 , #blank : 사용자가 한 입력이 비어있어도 허용하는 매개변수
    content = models.TextField('내용',null=True,blank=True)   
    pub_date = models.DateField('날짜',auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    class Meta:
        ordering = ('-id',) #ordering : Post 테이블 안의 객체들을 정렬하는 기준
    def __str__(self):
        return self.headline
    
class Image(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    image = models.ImageField('이미지파일', upload_to='uploads/%Y/%m/%d/content/')
    def __str__(self):
        return self.post.headline
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField('댓글')
    def __str__(self):
        return self.comment
    
    