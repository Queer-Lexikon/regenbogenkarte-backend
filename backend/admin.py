from django.contrib import admin

from .models import *

class OrganisationAdmin(admin.ModelAdmin):
    list_display = ["name", "country", "state"]
    list_filter = ["state__country", "state"]

class StateAdmin(admin.ModelAdmin):
    list_display = ["name", "country"]
    list_filter = ["country"]

admin.site.register(Organisation, OrganisationAdmin)
admin.site.register(Country)
admin.site.register(State, StateAdmin)

# Register your models here.
