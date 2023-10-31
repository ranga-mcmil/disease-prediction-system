from django.contrib import admin
from .models import Prediction
from import_export.admin import ExportActionMixin


# Register your models here.
@admin.register(Prediction)
class PredictionAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('id', 'created_by', 'symptom1', 'symptom2', 'symptom3', 'symptom4', 'symptom5', 'result', )
    list_filter = ('created_by',)
    search_fields = ('created_by', )
    raw_id_fields = ('created_by',)