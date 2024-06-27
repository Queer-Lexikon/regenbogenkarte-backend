from django.urls import path

from . import views

urlpatterns = [
        path("orgs.json", views.orgs_json),
]
