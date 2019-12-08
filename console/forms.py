from django import forms
from .models import SubjectAssign, SemAssign
from django.contrib.auth.models import User
from .models import Subject, Grade, Internal, Semester

class SubjectAssignForm(forms.ModelForm):
    class Meta:
        model = SubjectAssign
        fields = ['staff','subject']

class SemAssignForm(forms.ModelForm):
    class Meta:
        model = SemAssign
        fields = ['staff','semester']

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'
            
class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = '__all__'

class InternalForm(forms.ModelForm):
    class Meta:
        model = Internal
        fields = '__all__'

class SemesterForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = '__all__'