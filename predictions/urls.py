from django.urls import path, include
from . import views


app_name = 'predictions'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('symptoms/', views.SendSymptomsView.as_view(), name='send_symptoms'),
    path('reports/', views.ReportsView.as_view(), name='reports'),

]