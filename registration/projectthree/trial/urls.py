from django.urls import path
from . import views

urlpatterns=[
path(r'try1',views.try1,name='try'),
]