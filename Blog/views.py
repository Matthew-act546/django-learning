from typing import Any, Optional
from django.db import models
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)

from .forms import ArticleModelForm
from .models import Article


# Create your views here.
class ArticleListView(ListView):
    """Listing of all article."""
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all() # <blog>/<modelname>_list.html

class ArticleCreateView(CreateView):
    """Used to create an article."""
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all() 

    def form_valid(self, form):
        """if form valid will print the cleaned data of a form then return it valid(FORM)"""
        print(form.cleaned_data)
        return super().form_valid(form)
    
    def get_success_url(self):
        """redirecting to blog"""
        return '/blog/'

class ArticleDetailView(DetailView):
    """The full detail view of an article"""
    template_name = 'articles/article_detail.html'
    queryset = Article.objects.all() 

    def get_object(self):
        """Getting id to have access in the articles"""
        id_ = self.kwargs.get('my_id')
        # print(id_)
        return get_object_or_404(Article, id=id_)

class ArticleUpdateView(UpdateView):
    """Updating an article"""
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all() 

    def get_object(self):
        id_ = self.kwargs.get('my_id')
        return get_object_or_404(Article, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
    def get_success_url(self):
        return '/blog/'
    
class ArticleDeleteView(DeleteView):
    """Deleting an article"""
    template_name = 'articles/article_delete.html'
    queryset = Article.objects.all() 
    
    def get_object(self):
        id_ = self.kwargs.get('my_id')
        # print(id_)
        return get_object_or_404(Article, id=id_)
    
    def get_success_url(self):
        return reverse('articles:article-list')