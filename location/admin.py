from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import *


class LocationVillageAdmin(admin.ModelAdmin):
    list_display = ('id_okmot', 'name_village')


admin.site.register(LoationCountry)
admin.site.register(LocationOblast)
admin.site.register(LocationRegion)
admin.site.register(LocationOkmot)
admin.site.register(LocationVillage, LocationVillageAdmin)
