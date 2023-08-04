from django.contrib import messages
from django.shortcuts import render, redirect

from .form import Departmentform, bookingform, ReviewForm, Maindateform
from .models import departmentss, docterdetails, Review, Maindate


# Create your views here.
def home(request):
    return render(request,"Home.html")
def about(request):
    return render(request,'aboutus.html')
def team(request):
    dicts={'value':docterdetails.objects.all()}
    return render(request,'ourteam.html',dicts)
def Book(request):
    if request.method=='POST':
        formname=bookingform(request.POST)
        if formname.is_valid():
            formname.save()
            messages.success(request,'successfullyBooking')
    formname=bookingform
    return render(request,'booking.html',{'formname':formname})
def contact(request):
    return render(request,'contacts.html')
def department(request):
    dicts={'data':departmentss.objects.all()}
    return render(request,'department.html',dicts)
def details(request,myid):
    detai=docterdetails.objects.filter(id=myid).first()

    if request.method=="POST":
        formreview = ReviewForm(request.POST)
        if formreview.is_valid():
            formreview.save()
    value=Review.objects.all()

    formreview = ReviewForm()
    return render(request,'docterdetails.html',{'detai':detai,'formreview':formreview,'value':value})
def fromdjango(request):
    if request.method=='POST':
        form=Departmentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department')

    else:
        form=Departmentform()
    return render(request,'formdjango.html',{"form":form})

def reviwss(request):
    formreview=ReviewForm()
    return render(request,'docterdetails.html',{'formreview':formreview})

def date(request):
    da = {"val":Maindate.objects.all()}

    forms=Maindateform
    return render(request,'date.html',{'forms':forms})