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