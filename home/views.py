from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contacts
from django.contrib import messages
# Create your views here.
def index(request):
    context={
        'variable':"this is sent",
        'hello': "Hello DRC, the best programmer."
    }
    return render(request,'index.html',context)
    #return HttpResponse("This is homepage.")
def about(request):
    return render(request,'about.html')
def services(request):
    return render(request,'services.html')
def contacts(request):
    if request.method=="POST":
        email=request.POST.get('email')
        desc=request.POST.get('desc')
        contacts=Contacts(email=email, desc=desc, date=datetime.today())
        contacts.save()
        messages.success(request, 'Your details have been shared!!!')

    return render(request,'contacts.html')