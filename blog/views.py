from django.shortcuts import render, get_object_or_404
from .models import Article
def index(request):
    article = Article.objects.filter(isPublished="publish")
    context = {
        "article": article,
    }
    return render(request, "index.html", context)
