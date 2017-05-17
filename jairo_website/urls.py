from django.conf.urls import url

from . import views

app_name = 'jairo_website'
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^about/$', views.about, name = 'about'),
    url(r'^memes/$', views.memes, name = 'memes'),
]