from django.contrib import admin

# Register your models here.
from .models import departmentss, Maindate
from .models import docterdetails
from .models import booking22
from .models import Review

admin.site.register(departmentss)
admin.site.register(docterdetails)
class bookingadmin(admin.ModelAdmin):
    list_display = ('PatientName','PatientPhone','PatientEmail','docname','dateall')

admin.site.register(booking22,bookingadmin)
admin.site.register(Review)
admin.site.register(Maindate)

