from django.contrib import admin
from .models import About, Article, Contact
# Register your modefls here.
admin.site.register(Article)
admin.site.register(Contact)
admin.site.register(About)

