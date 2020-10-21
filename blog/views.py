from django.shortcuts import render, get_object_or_404
from .models import Article
def index(request):
    article = Article.objects.filter(isPublished="publish")
    context = {
        "article": article,
    }
    return render(request, "index.html", context)


    
def detail(request, id=None):
	article = get_object_or_404(Article, id=id, isPublished="publish")
	context = {
		"article": article,
	}
	return render(request, "detail.html", context)