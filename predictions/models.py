from django.db import models
from accounts.models import User
from .utils import SYMPTOMS

class Prediction(models.Model):
    symptom1  = models.CharField(max_length=50, choices=SYMPTOMS)
    symptom2 = models.CharField(max_length=50, choices=SYMPTOMS)
    symptom3 = models.CharField(max_length=50, choices=SYMPTOMS)
    symptom4 = models.CharField(max_length=50, choices=SYMPTOMS)
    symptom5 = models.CharField(max_length=50, choices=SYMPTOMS)
    result = models.CharField(max_length=50)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="predictions")