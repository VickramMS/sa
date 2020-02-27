from django import forms
from users.models import User
from django.contrib.auth.forms import UserCreationForm


class AddStudentForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'department', 'user_type', 'email', 'date_of_birth', 'password1', 'password2']

class AddStaffForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'
