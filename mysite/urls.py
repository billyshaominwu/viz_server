"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include, path
from . import views

urlpatterns = [
    path('mysite/', include('mysite.crimesapp.urls')),
    path('admin/', admin.site.urls),
    path('crimes/<str:longitude>/<str:latitude>/<str:radius>', views.get_crime_frequency_in_circle),
    path('crimes/year/<str:longitude>/<str:latitude>/<str:radius>', views.get_crime_frequency_by_year)
]
