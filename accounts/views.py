from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic.edit import CreateView
from .models import User
from core.logger import logger
from .forms import UserForm

# Create your views here.
class RegisterView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'registration/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('predictions:home')
