import os
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.contrib.auth import logout
# Create your views here.
def first(request):
    return HttpResponse('my first django page')

def register1(request):
    if request.method=='POST':
        a=reg1form(request.POST,request.FILES)
        if a.is_valid():
            fn=a.cleaned_data['firstname']
            ln=a.cleaned_data['lastname']
            un=a.cleaned_data['username']
            em=a.cleaned_data['email']
            pn=a.cleaned_data['phone']
            ac=int('15'+str(pn))
            fl=a.cleaned_data['file']
            ps=a.cleaned_data['pin']
            cps=a.cleaned_data['pinn']
            if ps==cps:
                b=regmodel1(firstname=fn,lastname=ln,username=un,email=em,phone=pn,file=fl,pin=ps,balance=0,account=ac)
                b.save()
                subject = 'your account has been created'
                message = f'your new account number is {ac}'
                email_from = 'shuhaibvkp24@gmail.com'
                email_to = em
                send_mail(subject, message, email_from, [email_to])
                return redirect(login_view)
            else:
                 return HttpResponse('file upload file')
        else:
             return HttpResponse('registration failed')
    return render(request,"reg.html")

def login_view(request):
    if request.method=='POST':
        a=logform(request.POST)
        if a.is_valid():
            un=a.cleaned_data['username']
            p=a.cleaned_data['pin']
            b=regmodel1.objects.all()
            for i in b:
                if i.username==un and i.pin==p:
                    request.session['id']=i.id
                    return redirect(profile)
            else:
                return redirect(login_view)

    return render(request,'login.html')

def profile(request):
    try:
        id1 = request.session['id']
        a = regmodel1.objects.get(id=id1)
        img = str(a.file).split('/')[-1]
        return render(request, 'profile.html', {'a': a, 'img': img})


    except:
        return redirect(login_view)




def editdata(request,id):
    a=regmodel1.objects.get(id=id)
    if request.method=='POST':
        a.firstname=request.POST.get('firstname')
        a.lastname = request.POST.get('lastname')
        a.email = request.POST.get('email')
        a.phone = request.POST.get('phone')
        a.save()
        return redirect(profile)
    return render(request,'editdetails.html',{'a':a})


def fileedit(request,id):
    a=regmodel1.objects.get(id=id)
    img=str(a.file).split('/')[-1]
    if request.method=='POST':
        a.username=request.POST.get('username')
        if len(request.FILES)!=0:
            if len(a.file)!=0:
                os.remove(a.file.path)
            a.file=request.FILES['file']
        a.save()
        return redirect(profile)
    return render(request,'fileupload.html',{'a':a,'img':img})

def addmoney(request,id):
    x=regmodel1.objects.get(id=id)
    if request.method=='POST':
        am=request.POST.get('balance') #withot form
        x.balance +=int(am)
        x.save()
        b = addamount(amount=am,uid=request.session['id'] )
        b.save()
        request.session['am'] = am
        request.session['ac']=x.account
        pin = request.POST.get('pin')
        if pin==x.pin:
            return redirect(success)
        else:
            return HttpResponse('failed')
    return render(request,'addamount.html')


def success(request):
    am=request.session['am']
    ac=request.session['ac']
    return render(request,'amountsuccess.html',{'am':am,'ac':ac})


def widrawmoney(request,id):
    x=regmodel1.objects.get(id=id)
    if request.method=='POST':
        am = request.POST.get('balance')  # withot form
        request.session['am'] = am
        request.session['ac'] = x.account
        pin = request.POST.get('pin')
        if pin == x.pin:

         if(x.balance>=int(am)):
            x.balance -= int(am)
            x.save()
            b = withmoney(amount=am,uid=request.session['id'])
            b.save()
            return redirect(widrawdisplay)

         else:
            return HttpResponse('insufficient balance')
        else:
            return HttpResponse('password incorrect')

    return render(request,'withdrawamount.html')
def widrawdisplay(request):
    am=request.session['am']
    ac=request.session['ac']
    return render(request,'withdrawsuccess.html',{'am':am,'ac':ac})

def checkbalance(request,id):
    a=regmodel1.objects.get(id=id)
    if request.method=='POST':
        request.session['balance']=a.balance
        request.session['ac']=a.account
        pin=request.POST.get('pin')
        if pin==a.pin:
            return redirect(checkbalance1)
        else:
            return HttpResponse('wrong passsword')
    return render(request,'checkbalance.html')
def checkbalance1(request):
    ac=request.session['ac']
    balance=request.session['balance']
    return render(request,'checkbalanceshow.html',{'ac':ac,'balance':balance})


def statement(request,id):
    a=regmodel1.objects.get(id=id)
    pin = request.POST.get('pin')
    if request.method=='POST':
        if pin ==a.pin:
            choice=request.POST.get('statement')
            if choice=='deposit':
                return redirect(depdisplay)
            elif choice=='withdraw':
                return redirect(withdisplay)
        else:
            return HttpResponse('PASSSWORD ERROR')
    return render(request, 'ministatment.html')


def depdisplay(request):
    x=addamount.objects.all() #fetchall
    id=request.session['id']
    return render(request,'amountdisplay.html',{'x':x,'id':id})

def withdisplay(request):
    id = request.session['id']
    x=withmoney.objects.all()

    return render(request,'withdrawstatement.html',{'x':x,'id':id})

def news(request):
    if request.method=='POST':
        a=newsform(request.POST)
        if a.is_valid():
            top=a.cleaned_data['topic']
            con=a.cleaned_data['content']
            b=newsmodel(topic=top,content=con)
            b.save()
            return redirect(newsdisplay)
        else:
            return HttpResponse('failed')
    return render(request,'newsfeed.html')

def display(request):
    a = newsmodel.objects.all()
    return render(request, 'newsdisplay.html', {'a': a})


def admin(request):
    if request.method=='POST':
        a=adminform(request.POST)
        if a.is_valid():
            username=a.cleaned_data['username']
            password=a.cleaned_data['pin']
            User=authenticate(request,username=username,password=password)
            if User is not None:
                return render(request,'admindisplay.html')
            else:
                return HttpResponse('login failed')
    return render(request,'adminlogin.html')
def index(request):
    return render(request,'frontpage.html')



def adminnewsdelete(request,id):
    a=newsmodel.objects.get(id=id)
    a.delete()
    return redirect(newsdisplay)
def adminnewsedit(request,id):
    a=newsmodel.objects.get(id=id)
    if request.method=='POST':
        a.topic=request.POST.get('topic')
        a.content=request.POST.get('content')
        a.save()
        return redirect(newsdisplay)
    return render(request,'newsdisplayedit.html',{'a':a})

def newsdisplay(request):
    a=newsmodel.objects.all()
    return render(request,'adminnewsfeeddisplay.html',{'a':a})

def wish(request,id):
    a=newsmodel.objects.get(id=id)
    a1=wishlist.objects.all()
    for i in a1:
        if i.newsid==a.id and i.uid==request.session['id']:
            return HttpResponse('Item already in wishlist')
    b=wishlist(topic=a.topic,content=a.content,date=a.date,newsid=a.id,uid=request.session['id'])
    b.save()
    return HttpResponse('added')

def wishlistview(request):
    a=wishlist.objects.all()
    id=request.session['id']
    return render(request,'wishlist.html',{'a':a,'id':id})

def logoutt(request):
    logout(request)
    return redirect(index)

def forgetpassword(request):
    a=regmodel1.objects.all()
    if request.method=='POST':
        em=request.POST.get('email')
        ac=request.POST.get('account')
        for i in a:
            if(i.email==em and i.account==int(ac)):
                id=i.id
                subject='password change'
                message=f'http://127.0.0.1:8000/bank_app/change/{id}'
                frm='shuhaibvkp24@gmail.com'
                to=em
                send_mail(subject,message,frm,[to])
                return HttpResponse('check email')
        else:
            return HttpResponse('sorry')

    return render(request,'forgotpassword.html')



def change_password(request,id):
    a=regmodel1.objects.get(id=id)
    if request.method=='POST':
        p1=request.POST.get('pin')
        p2=request.POST.get('repin')
        if p1==p2:
            a.pin=p1
            a.save()
            return HttpResponse('password changed')
        else:
            return HttpResponse('sorry')
    return render(request,'changepassw.html')


