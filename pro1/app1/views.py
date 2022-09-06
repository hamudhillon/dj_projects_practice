
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import blogPost
from .forms import Myform, Myform2
from .filters import myfilter
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

    if request.method=='POST':
        form=Myform2(request.POST or None,request.FILES or None)
        if form.is_valid:
            return HttpResponse('Submited')
    else:
        form=Myform2()

    return render(request,'emp.html',{'name':name,'form':form})

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

    myfilters=myfilter(request.GET,queryset=ob)
    ob=myfilters.qs
    context.update({
        'data':ob,
        'filter':myfilters
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


def myformview(request):
    
    if request.method=='POST':
        form=Myform(request.POST or None,request.FILES or None)
        if form.is_valid():
            ob=blogPost()
            name=form.cleaned_data['title']
            desc=form.cleaned_data['desc']
            post_by=form.cleaned_data['post_by']
            print(form.cleaned_data.get('image'))
            try:
                ob.image=form.cleaned_data['image']
            except:
                pass
            ob.title=name
            ob.desc=desc
            ob.post_by=post_by
            ob.save()
            return HttpResponse('/Submited/')
    else:
        form=Myform()
    return render(request,'dforms.html',{'form':form})
