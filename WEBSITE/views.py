__author__ = 'DELL'
from django.shortcuts import render
from .models import registertable,User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
def homepage(request):
    if request.method=="POST":
       
        
        uname= request.POST.get("uname")
        name=request.POST.get("name")
        #dept=request.POST.get("dept")
        #year=request.POST.get("year")

        email= request.POST.get("email")
        psw2=request.POST.get("psw2")
        reg_type= request.POST.get("reg_type")
        #registertable.objects.all().delete()

        
        
        data={"username":uname,"email":email,"name":name,"password":psw2,"type":reg_type}
        reg = registertable(uname=uname,name=name,email=email,password=psw2,reg_type=reg_type)

        reg.save()
        User.objects.create_user(uname, email, psw2)
        user = authenticate(username = uname, password = psw2)

        if reg_type=="student":
            return render(request,'Students/main_profile.html',data)
        elif reg_type=="teacher":
            return render(request,'Teachers/mainpage.html',data)
    return render(request,'homepage.html')
def loginn(request):
    
    username = password = ''
    if request.POST:
        username = request.POST.get('uname')
        password = request.POST.get('psw')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            if user.is_active:
                login(request, user)
                user=request.user
                
                userdata=registertable.objects.get(uname=username)
                print(userdata)
                if request.POST.get('remember'):   

                    request.session.set_expiry(180) # 2 weeks
                if userdata.reg_type=='student':
                    return render(request,"Students/main_profile.html")
                elif userdata.reg_type=='teacher':
                    return render(request,"Teachers/mainpage.html")
    return render(request,"homepage.html")
def logout(request):
    try:
        del request.session['member_id']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")
def email(request):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['maitrithaker2@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    return render(request,'homepage.html')














    