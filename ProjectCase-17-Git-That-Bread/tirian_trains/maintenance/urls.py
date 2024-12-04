from django.urls import path
from . import views

urlpatterns = [
    path('', views.maintenance_home, name='maintenance_home'),
    path('add-train/', views.add_train, name='add_train'),
    path('add-crew/', views.add_crew, name='add_crew'),
    path('add-maintenance-history/', views.add_maintenance_history, name='add_maintenance_history'),
]