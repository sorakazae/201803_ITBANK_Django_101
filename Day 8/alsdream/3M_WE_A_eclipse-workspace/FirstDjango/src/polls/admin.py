from django.contrib import admin #admin : 관리자 설정에 관한 기능이 있음

#해당 소스에서 모델 클래스를 알아야하기 때문에 import함
from polls import models

# Register your models here.
#관리자 페이지에서 테이블을 쓸 수 있도록 등록
admin.site.register(models.Choice)
admin.site.register(models.Question)
admin.site.register(models.Blog)
admin.site.register(models.Author)
admin.site.register(models.Entry)
