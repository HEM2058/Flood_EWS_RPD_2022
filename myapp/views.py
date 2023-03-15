from django.shortcuts import render,redirect
from myapp.models import *
from random import randint
# Create your views here.



def Base(request):
        return render (request,"base.html")
def Index(request):
    # if 'id' in request.session:
    #       id = request.session.get('id')
    #       if id:
    #        user = User.objects.get(id=id)
    #        return render(request,"index.html",{'user':user})
    #       else:
           st = Station.objects.all()
           return render(request,"index.html",{'st':st})



def Msg(request):
     
     if(request.method == "POST"):
             name = request.POST['name']
             contact = request.POST['contact']
             lat = request.POST.get('latitude')
             lng = request.POST.get('longitude')
             evacuation = request.POST['evacuation']

             msg = EvacuationMsg.objects.create(name=name, contact=contact, lat=lat, lng=lng ,evacuationNo=evacuation)
             sentmsg = "Your message has been sent.Wait a while to get response !"
             request.session['msg'] = sentmsg
             return redirect('index')
        
