"""djangosite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
#from django.conf.urls.static import static
from django.views import static
from django.views.generic.base import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('backend/', include('backend.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        path('',RedirectView.as_view(url="/index.html")),
        path('index.html', static.serve, {"path":"index.html", "document_root":settings.STATIC_ROOT}),
        re_path(r"^assets/(?P<path>.*)$", static.serve, {"document_root":settings.STATIC_ROOT + "/assets/"}),
    ]
