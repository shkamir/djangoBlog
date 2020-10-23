from django.contrib import admin
from .models import About, Article, Contact
# Register your modefls here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "isPublished","publish_date")
    list_filter = ("publish_date","isPublished",)
    search_fields = ("title", "description",)
    list_editable = ("isPublished",)
    class Meta:
        model = Article
        
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email",)
    list_filter = ("name","email",)
    search_fields = ("name", "message",)
    class Meta:
        model = Contact
        
class AboutAdmin(admin.ModelAdmin):
    search_fields = ("text",)
    class Meta:
        model = About


admin.site.register(Article, ArticleAdmin)

admin.site.register(Contact, ContactAdmin)

admin.site.register(About,AboutAdmin)

