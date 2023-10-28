from django import forms
from .models import Prediction
from django.forms import ChoiceField
from .utils import SYMPTOMS

class PredictionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.__class__ = ChoiceField
            field.choices = SYMPTOMS
            field.widget.attrs.update({'class': 'form-control'})
            
    class Meta:
        model = Prediction
        fields = ['symptom1', 'symptom2', 'symptom3', 'symptom4', 'symptom5']