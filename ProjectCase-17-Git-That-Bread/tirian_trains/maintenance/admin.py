from django.contrib import admin
from .models import Train, CrewInCharge, MaintenanceHistory

admin.site.register(Train)
admin.site.register(CrewInCharge)
admin.site.register(MaintenanceHistory)