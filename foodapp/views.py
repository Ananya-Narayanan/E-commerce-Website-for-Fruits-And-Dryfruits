from django.shortcuts import render,redirect
from foodapp.models import catdb,itemdb
from frontend.models import contactdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.contrib import messages

# Create your views here.

def foodpg(req):
    return render(req,"index.html")

def foodcat(req):
    return render(req,"addfruitdcategory.html")

def savecat(req):
    if req.method=="POST":
        cn=req.POST.get('cat')
        d=req.POST.get('desc')
        im=req.FILES['img']
        obj=catdb(Category=cn,Description=d,Image=im)
        obj.save()
        messages.success(req,"category saved successfully")
        return redirect(foodcat)

def discat(req):
    foodcat=catdb.objects.all()
    return render(req,"displayfruitcategory.html",{'foodcat':foodcat})

def editcat(req,dataid):
    foodedit=catdb.objects.get(id=dataid)
    return render(req,"editfruitcategory.html",{'foodedit':foodedit})

def updatecat(req,dataid):
    if req.method == "POST":
        cn = req.POST.get('cat')
        d = req.POST.get('desc')
        try:
            im = req.FILES['img']
            fs=FileSystemStorage()
            file=fs.save(im.name,im)
        except MultiValueDictKeyError:
            file=catdb.objects.get(id=dataid).Image
        catdb.objects.filter(id=dataid).update(Category=cn,Description=d,Image=file)
        messages.success(req, "updated  successfully")
        return redirect(discat)

def deletecat(req,dataid):
    fooddelete=catdb.objects.filter(id=dataid)
    fooddelete.delete()
    messages.warning(req, "category deleted successfully")
    return redirect(discat)

def fooditem(req):
    item=catdb.objects.all()
    return render(req,"additems.html",{'item':item})

def saveitem(req):
    if req.method=="POST":
        c=req.POST.get('cat')
        i=req.POST.get('item')
        d=req.POST.get('desc')
        p=req.POST.get('price')
        im=req.FILES['img']
        obj=itemdb(Category=c,Item=i,Description=d,Price=p,Image=im)
        obj.save()
        messages.success(req, "product saved successfully")
        return redirect(fooditem)

def disitem(req):
    data=itemdb.objects.all()
    return render(req,"displayfruititems.html",{'data':data})

def edititem(req,dataid):
    edit=itemdb.objects.get(id=dataid)
    item = catdb.objects.all()
    return render(req,"editfruititem.html",{'edit':edit,'item':item})

def updateitem(req,dataid):
    if req.method == "POST":
        c = req.POST.get('cat')
        i = req.POST.get('item')
        d = req.POST.get('desc')
        p = req.POST.get('price')
        try:
            im = req.FILES['img']
            fs=FileSystemStorage()
            file=fs.save(im.name,im)
        except MultiValueDictKeyError:
            file=itemdb.objects.get(id=dataid).Image
        itemdb.objects.filter(id=dataid).update(Category=c,Item=i,Description=d,Price=p,Image=file)
        messages.success(req, "updated  successfully")
        return redirect(disitem)

def deleteitem(req,dataid):
    dele=itemdb.objects.filter(id=dataid)
    dele.delete()
    messages.warning(req, "product deleted successfully")
    return redirect(disitem)

def adm(req):
    return render(req,"adminlogin.html")

def adminlog(request):
    if request.method=="POST":
        un=request.POST.get('user')
        pwd=request.POST.get('password')
        if User.objects.filter(username__contains=un).exists():
            user=authenticate(username=un,password=pwd)
            if user is not None:
                login(request,user)
                request.session['username']=un
                request.session['password']=pwd
                return redirect(foodpg)
            else:
                return redirect(adm)
        else:
            return redirect(adm)

def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(adm)

def viewcontact(req):
    data=contactdb.objects.all()
    return render(req,"viewcontact.html",{'data':data})

def deletecontact(req,dataid):
    delete=contactdb.objects.filter(id=dataid)
    delete.delete()
    return redirect(viewcontact)

def dis_iitem(req):
    return render(req,"dis_item.html")










