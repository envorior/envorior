from django.shortcuts import render,redirect
from generalapp.models import User
from publicapp.models import Profile,Post,Job,Donation,Complain,Notification
from datetime import date

# Create your views here.
def publichome(request):
    email=request.session['email']
    user = User.objects.get(email=email)
    profile = Profile.objects.get(user__email=email)
    #getitng all post
    post = Post.objects.all()
    #getting the post of current user
    user_post = Post.objects.filter(postby = profile.full_name)
    sum = 0
    for i in user_post:
        sum = sum +  int(i.reward)
        total_reward = sum
        print(total_reward)
    return render(request,'publichome.html',locals())

def uploadpost(request):
    user = request.session['email']
    #get details of user which wants to post
    profile = Profile.objects.get(user__email=user)
    postby = profile.full_name
    if request.method=='POST':
        caption = request.POST['caption']
        p_image = request.FILES['pimg']
        new_post=Post(postcaption=caption,postimage=p_image,postby=postby,posteddate = date.today(),reward=0)
        new_post.save()
        return redirect("publicapp:publichome")
    

    
def like_post(request,id):
    #user - current user
    user = request.session['email']
    post = Post.objects.filter(pid=id)
    #getting previous reward on post
    previous_reward = post[0].reward
    #adding one reward
    post = Post.objects.filter(pid=id).update(reward=previous_reward + 1)
    return redirect("publicapp:publichome")

def jobs(request):
    jobs = Job.objects.all()
    return render(request,'jobs.html',locals())

def uploadjob(request):
    user = request.session['email']
    job_by = User.objects.get(email=user)
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
                    job_by = job_by,
                    job_post_date=date.today())
        new_job.save()
        return redirect("publicapp:jobs")

def apply_job(request,id):
    user = request.session['email']
    job = Job.objects.get(j_id=id)
    job_by = job.job_by
    #getting email of user who posted the job
    job_by_email = job_by.email
    #getting the details of user who apply for job
    applicant = Profile.objects.get(user__email=user)
    applicant_name=applicant.full_name
    applicant_contact = applicant.contact_no
    msg = " Hii,{} apply for a job that you posted for {}. The details of applicant are as follows- Name = {} , contact_no = {}".format(applicant_name,job.job_type,applicant_name,applicant_contact)
    notification = Notification(n_msg=msg,notification_by=user,notification_to=job_by_email,notification_date=date.today())
    notification.save()
    return redirect("publicapp:jobs")


def about(request):
    return render(request,'about.html')
def complain(request):
    user = request.session['email']
    if request.method=='POST':
        complain_type=request.POST['complain_type']
        description=request.POST['description']
        complain_image=request.FILES['complain_image']
        complain_location=request.POST['location']
        complain_by = User.objects.get(email=user)
        new_complain = Complain(complain_by=complain_by,complain_type=complain_type,description=description,
                            complain_image=complain_image,complain_location=complain_location)
        new_complain.save()
    return render(request,'complain.html')

def contact(request):
    return render(request,'contact.html')

def donation(request):
    user = request.session['email']
    if request.method=='POST':
        donation_type=request.POST['donation_type']
        description=request.POST['description']
        product_image=request.FILES['p_image']
        donar_location=request.POST['location']
        donated_by = User.objects.get(email=user)
        donate = Donation(donation_type=donation_type,description=description,
                          product_image=product_image,
                          donar_location=donar_location,donated_by=donated_by)
        donate.save()
    return render(request,'donation.html')

def followers(request):
    return render(request,'followers.html')
def followings(request):
    return render(request,'followings.html')




def notifications(request):
    user = request.session['email']
    notifications = Notification.objects.filter(notification_to=user)
    return render(request,'notifications.html',locals())

def policy(request):
    return render(request,'policy.html')
def post(request):
    return render(request,'post.html')
def postjob(request):
    return render(request,'postjob.html')
def postdonation(request):
    return render(request,'postdonation.html')
def profile(request):
    return render(request,'profile.html')
def scam(request):
    return render(request,'scam.html')
def terms(request):
    return render(request,'terms.html')
