from django.contrib import admin

# Register your models here.
from .models import departmentss
from .models import docterdetails
admin.site.register(departmentss)
admin.site.register(docterdetails)
