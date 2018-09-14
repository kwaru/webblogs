"""defines the url of the blog app"""

from django.conf.urls import url
from . import views


urlpatterns=[
url(r'^$', views.index, name='index'),


]
