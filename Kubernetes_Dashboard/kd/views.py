from django.shortcuts import render
import sys
sys.path.append("..")
from src import getallpods
# Create your views here.
from django.shortcuts import HttpResponse,render
# Create your views here.
pod_details = getallpods.getallpods
poddetails = pod_details.getpods()
print(poddetails)
def kd_home(request):
    #return HttpResponse('<h1>Kubernetes Dashboard</h1>')

    context = {
        'pods' : poddetails
    }
    return render(request,'kd/homekd.html',context)
def podlist(request):
    #return HttpResponse('<h1>The podlist is as follows</h1>')
    return render(request, 'kd/podlist.html')