from django.shortcuts import render,redirect
from foodapp.models import catdb,itemdb
from frontend.models import contactdb,registerdb,cartdb
from django.contrib import messages

# Create your views here.
def homepg(req):
   cat=catdb.objects.all()
   return render(req,"home.html",{'cat':cat})

def propg(req):
   data=itemdb.objects.all()
   return render(req,"products.html",{'data':data})

def singlepro(req,proid):
   sdata=itemdb.objects.get(id=proid)
   return render(req,"singleproduct.html",{'sdata':sdata})

def profilter(req,cat_name):
   data=itemdb.objects.filter(Category=cat_name)
   return render(req,"productsfilter.html",{'data':data})

def about(req):
   return render(req,"aboutus.html")

def contact(req):
   return render(req,"contactus.html")

def services(req):
   return render(req,"services.html")

def savedata(req):
   if req.method=="POST":
      n=req.POST.get('name')
      e=req.POST.get('email')
      p=req.POST.get('phone')
      s=req.POST.get('subject')
      m=req.POST.get('message')
      obj=contactdb(Name=n,Email=e,Phone=p,Subject=s,Message=m)
      obj.save()
      return redirect(contact)

def register(req):
   return render(req,"register.html")

def saveregister(req):
   if req.method=="POST":
      n=req.POST.get('name')
      m=req.POST.get('mob')
      e=req.POST.get('email')
      u=req.POST.get('user')
      p=req.POST.get('pass')
      obj=registerdb(Name=n,Mobile=m,Email=e,Username=u,Password=p)
      obj.save()
      return redirect(register)

def userlogin(request):
   if request.method=="POST":
      un=request.POST.get('username')
      pwd=request.POST.get('password')
      if registerdb.objects.filter(Username=un,Password=pwd).exists():
         request.session['Username']=un
         request.session['Password']=pwd
         messages.success(request,"Logined successfully")


         return redirect(homepg)
      else:
         messages.warning(request,"Incorrect username/password")
         return redirect(register)

   return redirect(register)

def logout(request):
   del request.session['Username']
   del request.session['Password']
   return redirect(userlogin)

def cart(request):
   data=cartdb.objects.filter(username=request.session['Username'])
   total_price=0
   for i in data:
      total_price=total_price+i.totalprice
   return render(request,"cart.html",{'data':data,'total_price':total_price})

def delete_cart(request,dataid):
   dele=cartdb.objects.filter(id=dataid)
   dele.delete()
   return redirect(cart)


def save_cart(request):
   if request.method=="POST":
      pn=request.POST.get('pname')
      us=request.POST.get('user')
      p=request.POST.get('price')
      d=request.POST.get('desc')
      q=request.POST.get('qty')
      tp=request.POST.get('tprice')
      obj=cartdb(productname=pn,username=us,price=p,description=d,quantity=q,totalprice=tp)
      obj.save()
      return redirect(cart)

def checkout(request):
   data=cartdb.objects.filter(username=request.session['Username'])
   total_price = 0
   for i in data:
      total_price = total_price + i.totalprice
   return render(request,"checkout.html",{'data':data,'total_price':total_price})