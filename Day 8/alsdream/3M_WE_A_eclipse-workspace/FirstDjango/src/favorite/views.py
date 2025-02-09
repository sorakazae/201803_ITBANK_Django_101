from django.shortcuts import render
from .models import Favorite
from django.views.generic.list import ListView

# Create your views here.
class FavorList(ListView):
    pass

class FavorAdd:
    pass

class FavorDel:
    pass