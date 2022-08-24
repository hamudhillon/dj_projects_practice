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

def allpost(request):
    context={}

    ob=blogPost.objects.all()
    context.update({
        'data':ob,
    })    

    return render(request,'allpost.html',context)

def delete(request,id):

    ob=blogPost.objects.get(id=id)
    ob.delete()

    return redirect('allpost')
    
def edit(request,id):
    ob=blogPost.objects.get(id=id)
    if request.method=='POST':
        name=request.POST['Title']
        desc=request.POST['desc']
        
        try:
            request.FILES['Image']
            ob.image=request.FILES['Image']
        except:
            pass
        ob.title=name
        ob.desc=desc
        ob.save()
    
        return redirect('allpost')

    return render(request,'edit.html',{"data":ob})