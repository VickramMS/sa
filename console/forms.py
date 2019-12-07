from django import forms
from .models import SubjectAssign, SemAssign
from django.contrib.auth.models import User
from .models import Subject 

class SubjectAssignForm(forms.ModelForm):
    staff = forms.ModelChoiceField(queryset=User.objects.filter(is_staff=True))
    class Meta:
        model = SubjectAssign
        fields = ['staff','subject']

class SemAssignForm(forms.ModelForm):
    staff = forms.ModelChoiceField(queryset=User.objects.filter(is_staff=True))
    class Meta:
        model = SemAssign
        fields = ['staff','semester']
            