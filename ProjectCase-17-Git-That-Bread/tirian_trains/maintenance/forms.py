from django import forms
from .models import MaintenanceHistory

class MaintenanceHistoryForm(forms.ModelForm):
    class Meta:
        model = MaintenanceHistory
        fields = ['maintenance_id', 'task', 'condition', 'date_maintained', 'train', 'crew']