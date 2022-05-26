from rest_framework import permissions


class UserIsWorkingInTheSameCompany(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        is_admin = request.user.is_superuser or request.user.is_staff
        
        return True if is_admin else request.user.company==obj.company