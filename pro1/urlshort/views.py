from django.shortcuts import render,redirect
from .models import urls
from uuid import uuid4
# Create your views here.
def index(request):
    if request.method=='POST':
        long_url=request.POST['longurl']
        shortID=str(uuid4())[:5]
        ob=urls()
        ob.long_url=long_url
        ob.short_url_id=shortID
        ob.save()
        data=urls.objects.get(short_url_id=shortID)
        return render(request,'index.html',{'data':data})

    return render(request,'index.html',{})

def redirect_longURL(request,sid):
    ob=urls.objects.get(short_url_id=sid)

    return redirect(ob.long_url)
