from django.contrib import admin
from . import models
# Register your models here.


admin.site.register(models.Posttype) #admin사이트에서 모델클래스 조회, 수정, 삽입, 삭제 기능추가
admin.site.register(models.Post)
admin.site.register(models.Image)

