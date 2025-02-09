from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Boardtype)
admin.site.register(models.Board)
admin.site.register(models.File)
admin.site.register(models.Money)