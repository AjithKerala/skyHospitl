from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from new1 import views
urlpatterns = [
    path('',views.home,name='home'),
    path("about",views.about,name='about'),
    path('team', views.team, name='team'),
    path('Booking', views.Book, name='Booking'),
    path('Contact',views.contact,name="Contact"),
    path('department',views.department,name="department"),
    path('docterdetails/<int:myid>/',views.details,name="docterdetails")
    path('djangoform',views.)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
