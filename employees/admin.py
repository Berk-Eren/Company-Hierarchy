from .models import Employee

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


class EmployeeAdmin(UserAdmin):
    add_fieldsets = (
            (None, {
                'classes': ('wide',),
                'fields': ('username', 'password1', 'password2', 'company', 'position'),
            }),
        )

admin.site.register(Employee)