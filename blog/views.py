from django.shortcuts import render, get_object_or_404
from .models import Article, Contact, About
from django.contrib import messages



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
                "title":article.title,
	}
	return render(request, "detail.html", context)




def contact(request):

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        file = request.POST.get("file")
        # print (f"{name} has sent {message}")
        save_contact = Contact(name=name, email=email, message=message,file=file)
        save_contact.save()
       	messages.success(request,"successfilly sent")
        return render(request, "contact.html", {})
    else:
    	return render(request, "contact.html", {})
def about (request):
    about_text = About.objects.all()
    return render(request, "about.html", {"about": about_text})
