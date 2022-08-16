from django.urls import path
from .views import *
urlpatterns = [
    path('',index,name='Home'),
    path('emp/<str:name>',emp,name='emp'),
    path('post',post,name='post')
]
