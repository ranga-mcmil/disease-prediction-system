from django.shortcuts import render, redirect
from django.views.generic.base import TemplateResponseMixin, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PredictionForm
from .models import Prediction
from core.logger import logger
from core.predictions import predictions
from django.contrib import messages
from django.urls import reverse


# Create your views here.
class HomeView(LoginRequiredMixin, TemplateResponseMixin, View):
    template_name = 'predictions/home.html'
    
    def get(self, request, *args, **kwargs):
        reports_count = Prediction.objects.filter(created_by=request.user).count()
        return self.render_to_response({'reports_count': reports_count})

class SendSymptomsView(LoginRequiredMixin, TemplateResponseMixin, View):
    def post(self, request):
        form = PredictionForm(request.POST)

        if form.is_valid():
            prediction = form.save(commit=False)
            prediction.created_by = request.user
            symptoms = [prediction.symptom1, prediction.symptom2, prediction.symptom3, prediction.symptom4, prediction.symptom5] 
            results = predictions(symptoms)
            prediction.result = results[1]
            prediction = form.save()
            message_text = f'Symptoms: {prediction.symptom1}, {prediction.symptom2}, {prediction.symptom3}, {prediction.symptom4}, {prediction.symptom5} \n \n Prediction: {prediction.result}'
            messages.info(request, message_text)
            return redirect('predictions:home')
        else:  
            pass
        return redirect('predictions:home')


class ReportsView(LoginRequiredMixin, TemplateResponseMixin, View):
    template_name = 'predictions/reports.html'
    
    def get(self, request, *args, **kwargs):
        predictions = Prediction.objects.filter(created_by=request.user).order_by('-id')
        return self.render_to_response({'predictions': predictions})

