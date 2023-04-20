from django import forms

from new1.models import departmentss


class Departmentform(forms.Modelform):
    class Meta:
        models=departmentss
        fields=['name','des']
