from django.db import models
from django.utils import timezone
from django.utils.timezone import now


# Create your models here.
class departmentss(models.Model):
    name=models.CharField(max_length=100)
    des=models.TextField()
    def __str__(self):
        return self.name
class docterdetails(models.Model):
    images=models.ImageField(upload_to='main')
    docname=models.CharField(max_length=200)
    specilisation=models.CharField(max_length=200)
    name=models.ForeignKey(departmentss,on_delete=models.CASCADE)
    def __str__(self):
        return self.docname


class booking22(models.Model):
    PatientName=models.CharField(max_length=100)
    PatientPhone=models.IntegerField()
    PatientEmail=models.EmailField()
    docname=models.ForeignKey(docterdetails,on_delete=models.CASCADE)
    dateall=models.DateField(default=timezone.now)

class Review(models.Model):
    date=models.DateTimeField(default=now)
    text=models.CharField(max_length=100)

class Maindate(models.Model):

    val=models.DateField()


