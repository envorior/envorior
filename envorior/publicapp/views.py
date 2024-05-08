from django.shortcuts import render,redirect
from generalapp.models import User
from publicapp.models import Profile,Post,Job,Notification,Donation,Complain,TopEnvorior
from datetime import date
from django.views.decorators.cache import cache_control #validate thourgh server instead of browser
from django.http import JsonResponse



# Create your views here.
@cache_control(no_cache=True ,must_revalidate=True,no_store=True)
def publichome(request):
    try:
        if request.session['email']!=None:
            #common code for user details
            current_user = request.session['email']
            current_user_details = Profile.objects.get(user=current_user)
            top = TopEnvorior.objects.get(profile=current_user_details)
            total_reward = top.reward
            #top three envorior
            top_envorior = TopEnvorior.objects.order_by('-reward')[:8]

            #code for publichome
            post = Post.objects.all().order_by('-posteddate')
            return render(request,'publichome.html',locals())
        
    except KeyError:
        return redirect('generalapp:login')    
      
@cache_control(no_cache=True ,must_revalidate=True,no_store=True)
def uploadpost(request):
    try:
        if request.session['email']!=None:
            #common code for user details
            current_user = request.session['email']
            current_user_details = Profile.objects.get(user=current_user)
            top = TopEnvorior.objects.get(profile=current_user_details)
            total_reward = top.reward
            #top three envorior
            top_four_envorior = TopEnvorior.objects.order_by('-reward')[:4]

            #code for uploadpost
            if request.method=='POST':
                caption = request.POST['caption']
                p_image = request.FILES['pimg']
                Post.objects.create(postcaption=caption,postimage=p_image,postby=current_user_details,
                            posteddate = date.today())
                return redirect('publicapp:publichome')
    except KeyError:
        return redirect('generalapp:login')
    

def postform(request):
    #common code for user details
    current_user = request.session['email']
    current_user_details = Profile.objects.get(user=current_user)
    top = TopEnvorior.objects.get(profile=current_user_details)
    total_reward = top.reward
    #top  envorior
    top_envorior = TopEnvorior.objects.order_by('-reward')[:8] 
    return render(request,'post.html',locals())

def like_post(request,id):
    current_user = request.session['email']
    current_user_details = Profile.objects.get(user=current_user)
    user_instance = User.objects.get(email=current_user)
    post = Post.objects.filter(pid=id)
    if user_instance in post[0].likes.all():
        post[0].likes.remove(user_instance)
    else:
        post[0].likes.add(user_instance)

    #getting all rewards on donation
    current_user_donation = Donation.objects.filter(donated_by__full_name=current_user_details.full_name)
    total_reward_on_donation = 0
    for i in current_user_donation:
        a = i.rewards.count()
        total_reward_on_donation = total_reward_on_donation + a  
    #getting total reward onpost
    current_user_post = Post.objects.filter(postby__full_name=current_user_details.full_name)
    total_reward_on_post = 0
    for i in current_user_post:
        a = i.likes.count()
        total_reward_on_post = total_reward_on_post + a    
    #update total reward
    top = TopEnvorior.objects.get(profile=current_user_details)
    top.reward=total_reward_on_post+total_reward_on_donation
    top.save()

    return redirect("publicapp:publichome")

def jobs(request):
    #common code for user details
    current_user = request.session['email']
    current_user_details = Profile.objects.get(user=current_user)
    top = TopEnvorior.objects.get(profile=current_user_details)
    total_reward = top.reward
    #code for job  
    jobs = Job.objects.all() 
    #top  envorior
    top_envorior = TopEnvorior.objects.order_by('-reward')[:8]   
    return render(request,'jobs.html',locals())

def jobform(request):
    #common code for user details
    current_user = request.session['email']
    current_user_details = Profile.objects.get(user=current_user)
    top = TopEnvorior.objects.get(profile=current_user_details)
    total_reward = top.reward
    #top  envorior
    top_envorior = TopEnvorior.objects.order_by('-reward')[:8] 
    return render(request,'postjob.html',locals())

def uploadjob(request):
    #common code for user details
    current_user = request.session['email']
    current_user_details = Profile.objects.get(user=current_user)
    top = TopEnvorior.objects.get(profile=current_user_details)
    total_reward = top.reward
    #top  envorior
    top_envorior = TopEnvorior.objects.order_by('-reward')[:8] 

    #code for upload job   
    if request.method=='POST':
        skill_required = request.POST['skill']
        job_description = request.POST['description']
        job_type = request.POST['job_type']
        salary = request.POST['salary']
        job_location = request.POST['location']
        new_job=Job(skill_required=skill_required,
                    job_description=job_description,
                    job_type=job_type,salary=salary,
                    job_location=job_location,
                    job_by = current_user_details,
                    job_post_date=date.today())
        new_job.save()
        return redirect("publicapp:jobs")

def apply_job(request,id):
    #common code for user details
    current_user = request.session['email']
    current_user_details = Profile.objects.get(user=current_user)
    top = TopEnvorior.objects.get(profile=current_user_details)
    total_reward = top.reward
    #top  envorior
    top_envorior = TopEnvorior.objects.order_by('-reward')[:8] 

    #apply job code   
    #getting details of job by 
    job = Job.objects.get(j_id=id)
    job_by_name  = job.job_by.full_name
    job_by_profile = Profile.objects.get(full_name=job_by_name)
    job_by_email = job_by_profile.user.email

    #getting the details of user who apply for job
    applicant = Profile.objects.get(user__email=current_user)
    applicant_name=applicant.full_name
    applicant_contact = applicant.contact_no
    msg = " Hii,{} apply for a job that you posted for {}. The details of applicant are as follows- Name = {} , contact_no = {}".format(applicant_name,job.job_type,applicant_name,applicant_contact)
    notification = Notification(n_msg=msg,notification_by=current_user,notification_to=job_by_email,notification_date=date.today())
    notification.save()
    return redirect("publicapp:jobs")

def notifications(request):
    #common code for user details
    current_user = request.session['email']
    current_user_details = Profile.objects.get(user=current_user)
    top = TopEnvorior.objects.get(profile=current_user_details)
    total_reward = top.reward
    #top three envorior
    top_envorior = TopEnvorior.objects.order_by('-reward')[:8]

    #notification code   
    notifications = Notification.objects.filter(notification_to=current_user)
    return render(request,'notifications.html',locals())

def donation(request):
    #common code for user details
    current_user = request.session['email']
    current_user_details = Profile.objects.get(user=current_user)
    top = TopEnvorior.objects.get(profile=current_user_details)
    total_reward = top.reward
    #top  envorior
    top_envorior = TopEnvorior.objects.order_by('-reward')[:8] 
    #donation code  
    donation = Donation.objects.all() 
    return render(request,'donate.html',locals())

def postdonation(request):
    #common code for user details
    current_user = request.session['email']
    current_user_details = Profile.objects.get(user=current_user)
    top = TopEnvorior.objects.get(profile=current_user_details)
    total_reward = top.reward
    #top  envorior
    top_envorior = TopEnvorior.objects.order_by('-reward')[:8] 
    #post donation code   
    if request.method=='POST':
        donation_type=request.POST['donation_type']
        description=request.POST['description']
        product_image=request.FILES['p_image']
        donar_location=request.POST['location']
        donate = Donation(donation_type=donation_type,description=description,
                          product_image=product_image,
                          donar_location=donar_location,donated_by=current_user_details)
        donate.save()
    return render(request,'postdonate.html',locals())

def reward_donate(request,id):
    current_user = request.session['email']
    current_user_details = Profile.objects.get(user=current_user)
    user_instance = User.objects.get(email=current_user)

    donate = Donation.objects.filter(d_id=id)
    if user_instance in donate[0].rewards.all():
        donate[0].rewards.remove(user_instance)
    else:
        donate[0].rewards.add(user_instance)

    #getting all rewards on donation
    current_user_donation = Donation.objects.filter(donated_by__full_name=current_user_details.full_name)
    total_reward_on_donation = 0
    for i in current_user_donation:
        a = i.rewards.count()
        total_reward_on_donation = total_reward_on_donation + a  
    #getting total reward onpost
    current_user_post = Post.objects.filter(postby__full_name=current_user_details.full_name)
    total_reward_on_post = 0
    for i in current_user_post:
        a = i.likes.count()
        total_reward_on_post = total_reward_on_post + a    
    #update total reward
    top = TopEnvorior.objects.get(profile=current_user_details)
    top.reward=total_reward_on_post+total_reward_on_donation
    top.save()

    #common code for user details
    current_user = request.session['email']
    current_user_details = Profile.objects.get(user=current_user)
    top = TopEnvorior.objects.get(profile=current_user_details)
    total_reward = top.reward
    #top  envorior
    top_envorior = TopEnvorior.objects.order_by('-reward')[:8] 
    #donation code  
    donation = Donation.objects.all() 

    return render(request,'donate.html',locals())

def get_donation(request,id):
    #common code for user details
    current_user = request.session['email']
    current_user_details = Profile.objects.get(user=current_user)
    top = TopEnvorior.objects.get(profile=current_user_details)
    total_reward = top.reward
    #top  envorior
    top_envorior = TopEnvorior.objects.order_by('-reward')[:8] 
    #donation code  
    donation = Donation.objects.all() 

    #getting details of donar 
    donar = Donation.objects.get(d_id=id)
    donar_name  = donar.donated_by.full_name
    donar_profile = Profile.objects.get(full_name=donar_name)
    donar_email = donar_profile.user.email

    #getting the details of user who want donation
    applicant = Profile.objects.get(user__email=current_user)
    applicant_name=applicant.full_name
    applicant_contact = applicant.contact_no
    msg = " Hii,{} want the product ({}) that you donated.The product description is {}. The details of reciver are as follows- Name = {} , contact_no = {}".format(applicant_name,donar.donation_type,donar.description,applicant_name,applicant_contact)
    notification = Notification(n_msg=msg,notification_by=current_user,notification_to=donar_email,notification_date=date.today())
    notification.save()

    
    return render(request,'donate.html',locals())


def complain(request):
    #common code for user details
    current_user = request.session['email']
    current_user_details = Profile.objects.get(user=current_user)
    top = TopEnvorior.objects.get(profile=current_user_details)
    total_reward = top.reward
    #top  envorior
    top_envorior = TopEnvorior.objects.order_by('-reward')[:8] 
    #complain code    
    if request.method=='POST':
        complain_type=request.POST['complain_type']
        description=request.POST['description']
        complain_image=request.FILES['complain_image']
        complain_location=request.POST['location']
        new_complain = Complain(complain_by=current_user_details,complain_type=complain_type,description=description,
                            complain_image=complain_image,complain_location=complain_location)
        new_complain.save()
    return render(request,'complain.html',locals())

def logout(request):
    try:
        del request.session['email']
    except KeyError:
        return redirect('generalapp:login')   
    return redirect('generalapp:login') 


def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')


def followers(request):
    return render(request,'followers.html')
def followings(request):
    return render(request,'followings.html')
def policy(request):
    return render(request,'policy.html')


def profile(request):
    #common code for user details
    current_user = request.session['email']
    current_user_details = Profile.objects.get(user=current_user)
    top = TopEnvorior.objects.get(profile=current_user_details)
    total_reward = top.reward
    #top  envorior
    top_envorior = TopEnvorior.objects.order_by('-reward')[:8]
    return render(request,'profile.html',locals())

def changeuserprofile(request):
    #common code for user details
    current_user = request.session['email']
    current_user_details = Profile.objects.get(user=current_user)
    top = TopEnvorior.objects.get(profile=current_user_details)
    total_reward = top.reward
    #top  envorior
    top_envorior = TopEnvorior.objects.order_by('-reward')[:8]

    #change_profile
    if request.method=='POST':
        profile_image=request.FILES['pic']
        current_user_details.profile_picture=profile_image
        current_user_details.save()
    return render(request,'profile.html',locals())

def show_user_post(request):
    #common code for user details
    current_user = request.session['email']
    current_user_details = Profile.objects.get(user=current_user)
    top = TopEnvorior.objects.get(profile=current_user_details)
    total_reward = top.reward
    #top  envorior
    top_envorior = TopEnvorior.objects.order_by('-reward')[:8]

    #getting post of user
    post = Post.objects.filter(postby=current_user_details).order_by('-posteddate')

    return render(request,'user_post.html',locals())

def deletepost(request,id):
    #common code for user details
    current_user = request.session['email']
    current_user_details = Profile.objects.get(user=current_user)
    top = TopEnvorior.objects.get(profile=current_user_details)
    total_reward = top.reward
    #top  envorior
    top_envorior = TopEnvorior.objects.order_by('-reward')[:8]

    #deletepost code
    post_for_delete = Post.objects.filter(pid=id)
    post_for_delete.delete()
    #getting post of user
    post = Post.objects.filter(postby=current_user_details).order_by('-posteddate')
    return render(request,'user_post.html',locals())



def show_user_complain(request):
    #common code for user details
    current_user = request.session['email']
    current_user_details = Profile.objects.get(user=current_user)
    top = TopEnvorior.objects.get(profile=current_user_details)
    total_reward = top.reward
    #top  envorior
    top_envorior = TopEnvorior.objects.order_by('-reward')[:8]

    #getting complain of user
    complain = Complain.objects.filter(complain_by=current_user_details)
    return render(request,'user_complain.html',locals())

def deletecomplain(request,id):
    #common code for user details
    current_user = request.session['email']
    current_user_details = Profile.objects.get(user=current_user)
    top = TopEnvorior.objects.get(profile=current_user_details)
    total_reward = top.reward
    #top  envorior
    top_envorior = TopEnvorior.objects.order_by('-reward')[:8]

    #deletecomplain code
    complain_for_delete = Complain.objects.filter(c_id=id)
    complain_for_delete.delete()

    #getting complain of user
    complain = Complain.objects.filter(complain_by=current_user_details)
    return render(request,'user_complain.html',locals())

def show_user_job(request):
    #common code for user details
    current_user = request.session['email']
    current_user_details = Profile.objects.get(user=current_user)
    top = TopEnvorior.objects.get(profile=current_user_details)
    total_reward = top.reward
    #top  envorior
    top_envorior = TopEnvorior.objects.order_by('-reward')[:8]

    #getting job of user
    jobs = Job.objects.filter(job_by=current_user_details)
    return render(request,'user_job.html',locals())

def deletejob(request,id):
    #common code for user details
    current_user = request.session['email']
    current_user_details = Profile.objects.get(user=current_user)
    top = TopEnvorior.objects.get(profile=current_user_details)
    total_reward = top.reward
    #top  envorior
    top_envorior = TopEnvorior.objects.order_by('-reward')[:8]

    #delete job code
    job_for_delete = Job.objects.filter(j_id=id)
    job_for_delete.delete()

    #getting job of user
    jobs = Job.objects.filter(job_by=current_user_details)
    return render(request,'user_job.html',locals())

def show_user_donation(request):
    #common code for user details
    current_user = request.session['email']
    current_user_details = Profile.objects.get(user=current_user)
    top = TopEnvorior.objects.get(profile=current_user_details)
    total_reward = top.reward
    #top  envorior
    top_envorior = TopEnvorior.objects.order_by('-reward')[:8]

    #getting donation of user
    donation = Donation.objects.filter(donated_by=current_user_details)
    return render(request,'user_donation.html',locals())

def deletedonation(request,id):
    #common code for user details
    current_user = request.session['email']
    current_user_details = Profile.objects.get(user=current_user)
    top = TopEnvorior.objects.get(profile=current_user_details)
    total_reward = top.reward
    #top  envorior
    top_envorior = TopEnvorior.objects.order_by('-reward')[:8]

    #delete donation code
    donation_for_delete = Donation.objects.filter(d_id=id)
    donation_for_delete.delete()

    #getting donation of user
    donation = Donation.objects.filter(donated_by=current_user_details)
    return render(request,'user_donation.html',locals())

def scam(request):
    return render(request,'scam.html')
def terms(request):
    return render(request,'terms.html')
