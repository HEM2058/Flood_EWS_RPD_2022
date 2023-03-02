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




