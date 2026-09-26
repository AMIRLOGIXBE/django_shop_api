from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = ('username','email','is_staff','is_superuser','is_active','date_joined')

admin.site.register(CustomUser,CustomUserAdmin)