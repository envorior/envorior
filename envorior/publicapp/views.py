<<<<<<< HEAD
from django.shortcuts import render
from generalapp.models import Profile,User

# Create your views here.
def publichome(request):
    email=request.session['email']
    user = User.objects.get(email=email)
    profile = Profile.objects.filter(user__email=email)
    return render(request,'publichome.html',locals())

=======

from django.shortcuts import render

# Create your views here.
def publichome(request):
    return render(request,'publichome.html')
>>>>>>> 1c239607f22fe8c0decd8b5d29d10a429c48233f
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
