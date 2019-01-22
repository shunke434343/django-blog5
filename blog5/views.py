from django.views import generic
from django.shortcuts import render
from .models import Article

class IndexView(generic.ListView):
    model = Article
    paginate_by = 9

class DetailView(generic.DetailView):
    model = Article


# Create your views here.
