from django.shortcuts import render,redirect,reverse
from .models import User
from django.contrib import messages
from publicapp.models import Profile,TopEnvorior
from django.contrib.auth.hashers import make_password , check_password
import random
from django.core.mail import send_mail
from django.conf import settings



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
                messages.success(request,'Email Already Registered')
                return render(request,'registration.html',locals())
        except: 
                user=User(email=email,password=password)
                user.save()
                #password encryption
                current_user = User.objects.get(email=email)
                encrypted_password = make_password(current_user.password)
                print(encrypted_password)
                User.objects.filter(email=email).update(password = encrypted_password)

                profile=Profile(user=user,contact_no=contact_no,full_name=full_name,dob=dob,city=city,state=state,pin_code=pin_code)
                profile.save()
                top = TopEnvorior(profile = profile,reward=0).save()
                return render(request,'login.html')
    return render(request, 'registration.html')


def login(request):
    if request.method=='POST':
        email=request.POST['email']
        raw_password=request.POST['password']

        try:
            user=User.objects.get(email=email)
            hashed_password = user.password
            #password decrypt
            is_correct = check_password(raw_password, hashed_password)

            if user.email==email and is_correct and user.user_type=='general':
                request.session['email'] = email
                return redirect(reverse('publicapp:publichome'))
                    
            elif user.email==email and raw_password==hashed_password and user.user_type=='servent':
                request.session['email'] = email
                return redirect(reverse('serventapp:dashboard'))
                    
            elif user.email==email and raw_password==hashed_password  and user.user_type=='supervisor':
                request.session['email'] = email
                return redirect(reverse('supervisorapp:supervisordashboard'))
        except:
            messages.error(request,'Incorrect Email ID or Password')
            return render(request,'login.html',locals())        
    return render(request, 'login.html')


def forget_password(request):
    return render(request,'forgetpassword.html')

def get_otp(request):
    if request.method=='POST':
        email=request.POST['email']
        print(email)
        #get user details
        try:
            user=User.objects.get(email=email)
            user_profile = Profile.objects.get(user=user)
            random_number = random.randint(1111,9999)
            request.session['otp'] = random_number
            request.session['email'] = email
            subject='Forget Your password'
            msg=f'Hello, {user_profile.full_name} your OTP for Forget Password is  {random_number}.'
            email_from=settings.EMAIL_HOST_USER
            send_mail(subject, msg, email_from, [email])
            return render(request,'fill_otp.html')
        except:
            messages.error(request,'Incorrect Email ID or Email Id not registered')
            return render(request,'forgetpassword.html',locals())
    return render(request,'fill_otp.html')

def verify_otp(request):
    if request.method=='POST':
        user_otp=request.POST['otp']
        if int(user_otp) == request.session['otp']:
            return render(request,'change_password.html')
        else :
            messages.error(request,'Incorrect OTP')
            return render(request,'fill_otp.html',locals())

    return render(request,'forgetpassword.html')

def change_password(request):
    if request.method=='POST':
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if pass1 == pass2 :
            current_user = request.session['email']
            User.objects.filter(email = current_user).update(password=pass2)
            #password encryption
            user = User.objects.get(email=current_user)
            encrypted_password = make_password(user.password)
            print(encrypted_password)
            User.objects.filter(email=current_user).update(password = encrypted_password)
            return render(request,'login.html')

    return render(request,'forgetpassword.html')