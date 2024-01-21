from django.contrib import admin
from .models import User, RoleUser

# Register your models here.

class UserAdmni(admin.ModelAdmin):
    list_display = ['user_name', 'email', 'password', 'avatar', 'role_user', 'user_location']

admin.site.register(User, UserAdmni)
admin.site.register(RoleUser)