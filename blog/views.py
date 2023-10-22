from django.shortcuts import render
from .forms import ArticleForm
# Create your views here.
def article_form(request):
    return render(request, 'blog/article_form.html', {'form': ArticleForm})
def process_article(request):
    pass
def process_category(request):
    pass
def process_tag(request):
    pass
def article_list(request):
    pass
def tag_list(request):
    pass
def category_list(request):
    pass