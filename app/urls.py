from django.conf.urls import url
from . import views


#this is site's urls
urlpatterns = [
    url(r'^index', views.index, name='index'),
    url(r'^admin', views.admin)
]