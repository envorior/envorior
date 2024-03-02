from django.shortcuts import render,redirect
from .models import User,Profile

# Create your views here.
def registration(request):
    if request.method=='POST':
        email=request.POST['email']
        contact_no=request.POST['contact_no']
        full_name=request.POST['full_name']
        dob=request.POST['dob']
        state=request.POST['state']
        city=request.POST['city']
        pin_code=request.POST['pin_code']
        password=request.POST['password']

        try:
            check_email = User.objects.get(email=email)
            if check_email:
                print('Already registered')
                msg='Email already registered'
                return render(request,'registration.html',locals())
        except: 
                user=user(contact_no=contact_no,password=password)
                user.save()
                profile=Profile()
                profile.save(email=email,full_name=full_name,city=city)
                return render(request,'login.html')
    return render(request, 'registration.html')

def login(request):
    if request.method=='POST':
        contact_no=request.POST['contact_no']
        password=request.POST['password']
        try:
             contact_no=User.objects.get(contact_no=contact_no)
             if User.contact_no==contact_no and User.password==password:
                return redirect('publicapp:publichome')
        except:
            msg ='Incorrect Email ID or Password'
            return render(request,'login.html',locals())        
    return render(request, 'login.html')

