from django import forms

from new1.models import departmentss


class Departmentform(forms.ModelForm):
    class Meta:
        model = departmentss
        fields=['name','des']
