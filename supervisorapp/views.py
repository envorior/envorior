from django.shortcuts import render,redirect
from generalapp.models import User
from publicapp.models import Profile,Complain,TopEnvorior


def dashboard(request):
    try:
        if request.session['email']!=None:
            #common to all servent view
            current_user = request.session['email']
            current_user_details = Profile.objects.get(user=current_user)
            return render(request,'supervisor/pages/dashboard.html',locals())
    except KeyError:
        return redirect('generalapp:login')



def complain(request):
    #common to all servent view
    current_user = request.session['email']
    current_user_details = Profile.objects.get(user=current_user)
    #complain code
    complain = Complain.objects.filter(complain_status='unsolved')
    return render(request,'supervisor/pages/complain.html',locals())

def addservent(request):
    #common to all servent view
    current_user = request.session['email']
    current_user_details = Profile.objects.get(user=current_user)
    #add servent code
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        contact_no=request.POST['number']
        full_name=request.POST['department_type']
        state=request.POST['state']
        city=request.POST['city']
        pin_code=request.POST['pin_code']
        p_img = request.FILES['image']
        try:
            check_email = User.objects.get(email=email)
            if check_email:
                print('Already registered')
                msg='Email already registered'
                return render(request,'supervisor/pages/addservent.html',locals())
        except: 
                user=User(email=email,password=password,user_type='servent')
                user.save()
                profile=Profile(user=user,contact_no=contact_no,full_name=full_name,
                                city=city,state=state,pin_code=pin_code
                                ,profile_picture=p_img)
                profile.save()
                msg='Registration Successfully'
                return render(request,'supervisor/pages/addservent.html',locals())
        
    return render(request,'supervisor/pages/addservent.html',locals())



# this is for top social person
def rank(request):
    #common to all servent view
    current_user = request.session['email']
    current_user_details = Profile.objects.get(user=current_user)
    #top envorior code 
    top_envorior = TopEnvorior.objects.order_by('-reward')
    return render(request,'supervisor/pages/rank.html',locals())

def view_servent(request):
    #common to all servent view
    current_user = request.session['email']
    current_user_details = Profile.objects.get(user=current_user)
    #view ervent details
    servent = Profile.objects.filter(user__user_type='servent')
    return render(request,'supervisor/pages/viewservent.html',locals())
