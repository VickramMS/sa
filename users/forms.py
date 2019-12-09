from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class AddStudentForm(UserCreationForm):
    DEPT = (('MECH','Mechanical'), ('CIVIL','Civil'), ('EEE','Electrical and Electronics'), ('ECE','Electronics and Communication'), ('CSE','Computer Science and Engineering'),('OTHER','Others'))
    email = forms.EmailField(max_length=255,required=True)
    department = forms.ChoiceField(required=True, choices=DEPT)
    sem = forms.IntegerField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'department', 'sem']
    
    def __str__(self):
        return self.username

class AddStaffForm(UserCreationForm):
    DEPT = (('MECH','Mechanical'), ('CIVIL','Civil'), ('EEE','Electrical and Electronics'), ('ECE','Electronics and Communication'), ('CSE','Computer Science and Engineering'),('OTHER','Others'))
    email = forms.EmailField(max_length=255,required=True)
    department = forms.ChoiceField(required=True, choices=DEPT)

    class Meta:
        model = User
        
        fields = ['username', 'email', 'password1', 'password2', 'department']
    def save(self, commit=True):
        user = super (AddStaffForm , self ).save(commit=False)
        user.is_staff=True
        if commit :
            user.save()
        return user

    def __str__(self):
        return self.username
