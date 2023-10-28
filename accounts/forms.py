from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from django.contrib.auth.forms import UserCreationForm

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
        {'class': 'form-control '}
        )
        self.fields['password'].widget.attrs.update(
        {'class': 'form-control'}
        )

class UserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
            
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


