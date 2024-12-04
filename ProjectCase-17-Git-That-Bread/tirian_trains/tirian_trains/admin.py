from django.contrib import admin
from django.contrib.admin import AdminSite

class TirianTrainsAdminSite(AdminSite):
    site_header = "Tirian Trains Admin"
    site_title = "Tirian Trains Admin Portal"
    index_title = "Welcome to Tirian Trains Management"

admin_site = TirianTrainsAdminSite(name='tirian_admin')