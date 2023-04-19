from django.shortcuts import render

from .models import departmentss, docterdetails


# Create your views here.
def home(request):
    return render(request,"Home.html")
def about(request):
    return render(request,'aboutus.html')
def team(request):
    dicts={'value':docterdetails.objects.all()}
    return render(request,'ourteam.html',dicts)
def Book(request):
    return render(request,'booking.html')
def contact(request):
    return render(request,'contacts.html')
def department(request):
    dicts={'data':departmentss.objects.all()}
    return render(request,'department.html',dicts)
def details(request,myid):
    val={"detai":docterdetails.objects.filter(id=myid).first()}
    return render(request,'docterdetails.html',val)
