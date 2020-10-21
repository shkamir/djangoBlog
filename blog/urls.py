from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
	path("", views.index, name="index"),
	url(r"^more/(?P<id>[0-9]{1,})*/", views.detail, name="detail")
]
