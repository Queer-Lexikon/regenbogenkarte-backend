from django.contrib import admin

from .models import *

class OrgEmailInline(admin.TabularInline):
    model = OrgEmail
    extra = 1

class OrgPhoneInline(admin.TabularInline):
    model = OrgPhone
    extra = 1

class OrgWebsiteInline(admin.TabularInline):
    model = OrgWebsite
    extra = 1

class OrganisationAdmin(admin.ModelAdmin):
    list_display = ["name", "country", "state"]
    list_filter = ["state__country", "state"]
    fieldsets = [
            (
                None,
                {
                    "fields": ["name", "activities", "identities", "age_restriction"],
                },
            ),
            (
                "Location",
                {
                    "fields": ["state", "address", "lat", "lon", "lat_lon_approx"],
                },
            ),
        ]
    inlines = [OrgEmailInline, OrgPhoneInline, OrgWebsiteInline]

class StateAdmin(admin.ModelAdmin):
    list_display = ["name", "country"]
    list_filter = ["country"]

admin.site.register(Organisation, OrganisationAdmin)
admin.site.register(Country)
admin.site.register(State, StateAdmin)

# Register your models here.
