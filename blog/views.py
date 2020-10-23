from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Contact, About
from django.contrib import messages
from .forms import ContactForm


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




# def contact(request):

#     if request.method == "POST":
#         name = request.POST.get("name")
#         email = request.POST.get("email")
#         message = request.POST.get("message")
#         file = request.POST.get("file")
#         # print (f"{name} has sent {message}")
#         save_contact = Contact(name=name, email=email, message=message,file=file)
#         save_contact.save()
#        	messages.success(request,"successfilly sent")
#         return render(request, "contact.html", {})
#     else:
#     	return render(request, "contact.html", {})

def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST or None) 
        form.save()    
        name=form.cleaned_data.get("name")
       	messages.success(request,"successfilly sent")
        client = Contact.objects.filter(name=name)
        form = ContactForm()
        redirect("contact")
        return render(request, "contact.html", {"form": form, "client":client})
    else:
    	return render(request, "contact.html", {"form": form})


def about (request):
    about_text = About.objects.all()
    return render(request, "about.html", {"about": about_text})
