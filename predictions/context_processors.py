from .forms import PredictionForm

def base_data(request):
    data = {}
    data["prediction_form"] = PredictionForm() 
    return data

