from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import blogPost
# Create your views here.
def index(request):
    data=[
        'APPLE',
        'ORANGES',
        'GRAPES'
    ]
    return render(
        request,
        'index.html',
        {"data":data}
        )
def emp(request,name):
     return render(request,'emp.html',{'name':name})

def post(request):
    # if len(list(request.GET.values())):
    #     title=request.GET['Title']
    #     print(title)
    if request.method=='POST':
        print('Im Here in Post')
        name=request.POST['Title']
        desc=request.POST['desc']
        Image=request.FILES['Image']
        cat=request.POST['cat']
        ob=blogPost()
        ob.title=name
        ob.desc=desc
        ob.image=Image
        ob.save()
    return render(request,'Post.html')