from django.shortcuts import render,redirect
from  publicapp.models import Profile,Complain,TopEnvorior
from serventapp.models import Event
from datetime import date
from django.views.decorators.cache import cache_control


# Create your views here.
@cache_control(no_cache=True ,must_revalidate=True,no_store=True)
def dashboard(request):
    try:
        if request.session['email']!=None:
            #common to all servent view
            current_user = request.session['email']
            current_user_details = Profile.objects.get(user=current_user)
            return redirect('serventapp:complain')    
    except KeyError:
        return redirect('generalapp:login')     

def complain(request):
    #common to all servent view
    current_user = request.session['email']
    current_user_details = Profile.objects.get(user=current_user)
    #complain code
    complain = Complain.objects.all()
    return render(request,'servent/pages/complain.html',locals())

def solve_complain(request,id):
    #common to all servent view
    current_user = request.session['email']
    current_user_details = Profile.objects.get(user=current_user)
    #solve_complain code
    current_complain = Complain.objects.get(c_id=id)
    if current_complain.complain_status=='solved':
       current_complain.complain_status='unsolved'
       current_complain.save()
    elif current_complain.complain_status=='unsolved':
        current_complain.complain_status='solved' 
        current_complain.save()
    #getting all complain    
    complain = Complain.objects.all()    
    return render(request,'servent/pages/complain.html',locals()) 

def rank(request):
    #common to all servent view
    current_user = request.session['email']
    current_user_details = Profile.objects.get(user=current_user)
    #top envorior code 
    top_envorior = TopEnvorior.objects.order_by('-reward')
    return render(request,'servent/pages/rank.html',locals())


def servent(request):
    #common to all servent view
    current_user = request.session['email']
    current_user_details = Profile.objects.get(user=current_user)
    return render(request,'servent/pages/servent.html',locals())



def event(request):
    #common to all servent view
    current_user = request.session['email']
    current_user_details = Profile.objects.get(user=current_user)
    #event
    event = Event.objects.all().order_by('-date')
    return render(request,'servent/pages/event.html',locals())

def your_event(request):
    #common to all servent view
    current_user = request.session['email']
    current_user_details = Profile.objects.get(user=current_user)
    #event
    event = Event.objects.filter(department__user=current_user).order_by('-date')
    return render(request,'servent/pages/your_event.html',locals())

def delete_event(request,id):
    #common to all servent view
    current_user = request.session['email']
    current_user_details = Profile.objects.get(user=current_user)

    #deleteevent code
    event_for_delete =  Event.objects.filter(e_id=id)
    event_for_delete.delete()
    #getting event of user
    event = Event.objects.filter(department=current_user_details).order_by('-date')
    return render(request,'servent/pages/your_event.html',locals())

    


#view to post an event or news
def post(request):
    #common to all servent view
    current_user = request.session['email']
    current_user_details = Profile.objects.get(user=current_user)
    #post code
    if request.method=='POST':
        description=request.POST['description']
        image=request.FILES['image']
        event = Event(department=current_user_details,image=image,
                      description=description,date=date.today())
        event.save()
    return render(request,'servent/pages/post.html',locals())

def serventprofile(request):
    #common to all servent view
    current_user = request.session['email']
    current_user_details = Profile.objects.get(user=current_user)
    return render(request,'servent/pages/serventprofile.html',locals())

