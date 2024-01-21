from django.contrib import admin
from .models import *

# Register your models here.
class CharbaAdmin(admin.ModelAdmin):
    list_display = ['type_charba', 'code', 'code_chars', 'user', 'date_register']

admin.site.register(TypeCharba)
admin.site.register(Charba, CharbaAdmin)
admin.site.register(CharbaUpdate)