from django.shortcuts import render

def complain(request):
    return render(request,'servent/pages/complain.html')

def dashboard(request):
    return render(request,'servent/pages/dashboard.html')

def servent(request):
    return render(request,'servent/pages/servent.html')

def post(request):
    return render(request,'servent/pages/post.html')

def event(request):
    return render(request,'servent/pages/event.html')

def serventprofile(request):
    return render(request,'servent/pages/serventprofile.html')

def notification(request):
    return render(request,'servent/pages/notification.html')

def rank(request):
    return render(request,'servent/pages/rank.html')

