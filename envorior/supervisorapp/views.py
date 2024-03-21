from django.shortcuts import render

def complain(request):
    return render(request,'supervisor/pages/complain.html')

def dashboard(request):
    return render(request,'supervisor/pages/dashboard.html')


def addservent(request):
    return render(request,'supervisor/pages/addservent.html')

def event(request):
    return render(request,'supervisor/pages/event.html')


def notification(request):
    return render(request,'supervisor/pages/notification.html')

# this is for top social person
def rank(request):
    return render(request,'supervisor/pages/rank.html')

