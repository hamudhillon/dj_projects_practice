from django.http import HttpResponse
from django.shortcuts import render,redirect
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
        print(request.POST)
        title=request.POST['Title']
        image=request.FILES['Image']
        desc=request.POST['desc']
        cat=request.POST['cat']
        print(title)
        print(image)
        print(desc)
        print(cat)
    return render(request,'Post.html')