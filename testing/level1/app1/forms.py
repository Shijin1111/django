from django import forms
from app1.models import student,Teacher
from django.contrib.auth.models import User
class studentform(forms.ModelForm):
    class Meta:
        model = student
        fields = ['sname','age']

class teacherform(forms.ModelForm):
    username = forms.CharField(required=False)
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username','email','password')
        error_messages = {
            'username': {
                'required': 'Please enter your username.',
            },
            'email': {
                'required': 'Please enter your email address.',
            },
            'password': {
                'required': 'Please enter your password.',
            },
        }
    
        
class portForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('portfolio_site','profile_pic')
        