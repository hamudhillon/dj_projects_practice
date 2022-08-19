from django.urls import path
from .views import *
urlpatterns = [
    path('',index,name='Home'),
    path('emp/<str:name>',emp,name='emp'),
    path('post',post,name='post'),
    path('allpost',allpost,name='allpost'),
    path('delete/<int:id>',delete ,name='delete')
]
