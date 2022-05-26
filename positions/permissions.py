from rest_framework import permissions


class PositionIsPartOfTheCompany(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return True if request.user.is_superuser\
                        else request.user.company == obj.department.company