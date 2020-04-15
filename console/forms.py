from django import forms
from .models import IntAssign, SemAssign
from users.models import User
from .models import Subject, Grade, Internal, Semester

class IntAssignForm(forms.ModelForm):
    class Meta:
        model = IntAssign
        fields = ['staff','subject', 'department']

class SemAssignForm(forms.ModelForm):
    class Meta:
        model = SemAssign
        fields = ['staff','semester', 'department']

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'
            
class InternalForm(forms.ModelForm):
    class Meta:
        model = Internal
        fields = '__all__'
class SemesterForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = '__all__'