from django.db import models

# Create your models here.
class Favorite(models.Model):
    name = models.CharField('site',max_length=200)
    link = models.TextField('link')
    def __str__(self):
        return self.name