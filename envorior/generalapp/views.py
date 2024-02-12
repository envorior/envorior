from django.shortcuts import render,redirect
from .models import Registration,Login

# Create your views here.

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        try:
             user=Login.objects.get(email=username)
             if user.email==username and user.password==password:
                return redirect('publicapp:publichome')
        except:
            msg ='Incorrect Email ID or Password'
            return render(request,'login.html',locals())        
    return render(request, 'login.html')

def registration(request):
    if request.method=='POST':
        email=request.POST['email']
        contactno=request.POST['contactno']
        fname=request.POST['fname']
        lname=request.POST['lname']
        dob=request.POST['dob']
        gender=request.POST['gender']
        country=request.POST['country']
        state=request.POST['state']
        city=request.POST['city']
        pin=request.POST['pin']
        password=request.POST['password']

        try:
            check_email = Registration.objects.get(email=email)
            if check_email:
                print('Already registered')
                msg='Email already registered'
                return render(request,'registration.html',locals())
        except: 
                reg=Registration(email=email,fname=fname,contactno=contactno,lname=lname,dob=dob,gender=gender,country=country,state=state,city=city,pin=pin)
                reg.save()
                log=Login(email=email,password=password)
                log.save()
                return render(request,'login.html')
    return render(request, 'registration.html')