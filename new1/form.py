from datetime import datetime

from django import forms

from new1.models import departmentss, booking22, Review, Maindate


class Departmentform(forms.ModelForm):
    class Meta:
        model = departmentss
        fields=['name','des']




class bookingform(forms.ModelForm):

    class Meta:

        model=booking22
        fields='__all__'
class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields=['text']

#class DateInput(forms.DateInput):
 #   input_type='date'
class Maindateform(forms.ModelForm):

    class Meta:
        model=Maindate
        fields='__all__'
        widget = {


            'val': forms.DateInput(attrs={'format': 'yyyy-mm-dd', 'type': 'date'}),
             }






