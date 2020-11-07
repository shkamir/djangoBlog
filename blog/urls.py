from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
	path("", views.index, name="index"),
	url(r"^more/(?P<id>[0-9]{1,})*/", views.detail, name="detail"),
	path("contact", views.contact, name="contact"),
	url(r"^about$", views.about, name="about"),
	url(r"^signup", views.register, name="register"),
	url(r'^login$', views.login_user, name="login"),
	url(r'^logout$', views.logout_user, name="logout"),
]
