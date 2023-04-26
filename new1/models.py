from django.db import models

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
class doct(models.Model):
    imagess=models.ImageField(upload_to='doc')
    docname=models.CharField(max_length=200)
    department=models.CharField(max_length=200)
