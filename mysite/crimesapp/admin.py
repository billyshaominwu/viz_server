from django.contrib import admin

# Register your models here.

from .models import Crime
admin.site.register(Crime)