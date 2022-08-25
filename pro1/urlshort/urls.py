from django.urls import path
from .views import *
urlpatterns = [
    path('',index,name='Home'),
    path('shorturl/<str:sid>',redirect_longURL,name='Redirect')
]
