from django.contrib import admin
from .models import Suvai, Suvaichy


# Register your models here.

class SAdmin(admin.ModelAdmin):
    list_display = ['user', 'charba', 'date_start', 'date_end', 'price', 'suvachy']

    admin.site.register(Suvai)
    admin.site.register(Suvaichy)
