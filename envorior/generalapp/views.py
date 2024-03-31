from django.shortcuts import render,redirect,reverse
from .models import User
from publicapp.models import Profile,TopEnvorior

# Create your views here.
def registration(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        contact_no=request.POST['contact_no']
        full_name=request.POST['full_name']
        dob=request.POST['dob']
        state=request.POST['state']
        city=request.POST['city']
        pin_code=request.POST['pin_code']
        try:
            check_email = User.objects.get(email=email)
            if check_email:
                print('Already registered')
                msg='Email already registered'
                return render(request,'registration.html',locals())
        except: 
                user=User(email=email,password=password)
                user.save()
                profile=Profile(user=user,contact_no=contact_no,full_name=full_name,dob=dob,city=city,state=state,pin_code=pin_code)
                profile.save()
                top = TopEnvorior(profile = profile,reward=0).save()
                return render(request,'login.html')
    return render(request, 'registration.html')

def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        
        try:
             user=User.objects.get(email=email)
             print(email,password,user.user_type)
             if user.email==email and user.password==password and user.user_type=='general':
                request.session['email'] = email
                return redirect(reverse('publicapp:publichome'))
             
             elif user.email==email and user.password==password and user.user_type=='servent':
                request.session['email'] = email
                return redirect(reverse('serventapp:dashboard'))
             
             elif user.email==email and user.password==password and user.user_type=='supervisor':
                request.session['email'] = email
                return redirect(reverse('supervisorapp:supervisordashboard'))
        except:
            msg ='Incorrect Email ID or Password'
            return render(request,'login.html',locals())        
    return render(request, 'login.html')

