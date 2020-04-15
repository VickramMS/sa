from django import forms
from .models import IntAssign, SemAssign
from users.models import User
from .models import Subject, Grade, Internal, Semester

class InternalForm(forms.ModelForm):
    class Meta:
        model = Internal
        fields = '__all__'
        
class SemesterForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = '__all__'