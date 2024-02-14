from django.shortcuts import render

def dashboardparent(request):
    return render(request,'dashboardparent.html')

def servent(request):
    return render(request,'servent.html')

def post(request):
    return render(request,'post.html')

def event(request):
    return render(request,'event.html')

def serventprofile(request):
    return render(request,'serventprofile.html')

def notification(request):
    return render(request,'notification.html')

def rank(request):
    return render(request,'rank.html')
