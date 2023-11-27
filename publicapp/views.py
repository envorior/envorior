from django.shortcuts import render

# Create your views here.
def publichome(request):
    return render(request,'publichome.html')