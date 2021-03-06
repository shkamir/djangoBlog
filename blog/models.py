from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
# Create your models here.
class Article(models.Model):
    # title, description, published, update, draft | publish
    STATUS = (
        ("publish", "publish"),
        ("draft", "draft"),
    )
    title = models.CharField(max_length=200)
    description = RichTextUploadingField()
    publish_date = models.DateTimeField(auto_now=True)
    isPublished = models.CharField(
        max_length=50,
        choices = STATUS,
        default = "d",
    )
    def __str__(self):
        return f"{self.title}-{self.isPublished}"

    def get_absolute_url(self):
        return reverse("detail", args=[str(self.id)])
    
    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Article's"


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    file = models.FileField(blank=True, null=True)
    class Meta:
        verbose_name = "contact"
        verbose_name_plural = "contact form's"
class About(models.Model):
    # about text
    text = RichTextUploadingField()
    def __str__(self):
        return "about text id --- {}".format(self.id)
    
    class Meta:
        verbose_name = "About Text"
        verbose_name_plural = "About"
