from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class AddStudentForm(UserCreationForm):
    DEPT = (('MECH','Mechanical'), ('CIVIL','Civil'), ('EEE','Electrical and Electronics'), ('ECE','Electronics and Communication'), ('CSE','Computer Science and Engineering'),('OTHER','Others'))
    email = forms.EmailField(max_length=255,required=True)
    is_staff = forms.BooleanField(initial=False, required=False)
    department = forms.ChoiceField(required=True, choices=DEPT)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def __str__(self):
        return self.username

class AddStaffForm(UserCreationForm):
    email = forms.EmailField(max_length=255,required=True)
    is_staff = forms.BooleanField(initial=False, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def __str__(self):
        return self.username
