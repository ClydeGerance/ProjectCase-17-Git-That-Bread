from django.shortcuts import render, redirect
from .models import Train, MaintenanceHistory, CrewInCharge
from .forms import MaintenanceHistoryForm
from django import forms

def maintenance_home(request):
    return render(request, 'maintenance/home.html')

# Forms for Train and CrewInCharge
class TrainForm(forms.ModelForm):
    class Meta:
        model = Train
        fields = [
            'train_id', 'model', 'max_speed', 'no_of_seats', 'no_of_toilets', 
            'has_reclining_seats', 'has_folding_tables', 'has_disability_access', 
            'has_luggage_storage', 'has_vending_machines', 'has_food_service'
        ]

class CrewInChargeForm(forms.ModelForm):
    class Meta:
        model = CrewInCharge
        fields = ['crew_id', 'leader_fn', 'leader_ln']

# Unified Train Page (Form + List)
def add_train(request):
    if request.method == 'POST':
        form = TrainForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_train')
    else:
        form = TrainForm()

    trains = Train.objects.all()  # Fetch list of trains
    return render(request, 'maintenance/add_train.html', {'form': form, 'trains': trains})

# Unified Crew Page (Form + List)
def add_crew(request):
    if request.method == 'POST':
        form = CrewInChargeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_crew')
    else:
        form = CrewInChargeForm()

    crew = CrewInCharge.objects.all()  # Fetch list of crew members
    return render(request, 'maintenance/add_crew.html', {'form': form, 'crew': crew})

# Unified Maintenance History Page (Form + List)
def add_maintenance_history(request):
    if request.method == 'POST':
        form = MaintenanceHistoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_maintenance_history')
    else:
        form = MaintenanceHistoryForm()

    maintenance_history = MaintenanceHistory.objects.select_related('train', 'crew').all()  # Fetch list of maintenance history
    return render(request, 'maintenance/add_maintenance_history.html', {
        'form': form,
        'maintenance_history': maintenance_history
    })