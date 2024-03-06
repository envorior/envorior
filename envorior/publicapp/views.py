from django.shortcuts import render
from generalapp.models import User
from publicapp.models import Profile,Post

# Create your views here.
def publichome(request):
    email=request.session['email']
    user = User.objects.get(email=email)
    profile = Profile.objects.get(user__email=email)
    post = Post.objects.all()
    return render(request,'publichome.html',locals())




def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def donation(request):
    return render(request,'donation.html')
def jobs(request):
    return render(request,'jobs.html')
def policy(request):
    return render(request,'policy.html')
def scam(request):
    return render(request,'scam.html')
def terms(request):
    return render(request,'terms.html')
def profile(request):
    return render(request,'profile.html')
def complain(request):
    return render(request,'complain.html')
def followers(request):
    return render(request,'followers.html')
def followings(request):
    return render(request,'followings.html')
def notifications(request):
    return render(request,'notifications.html')
