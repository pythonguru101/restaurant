from rest_framework.permissions import BasePermission
from user.enums import RoleChoice


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == RoleChoice.ADMIN.value


class IsEmployee(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == RoleChoice.EMPLOYEE.value


class IsOwner(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == RoleChoice.OWNER.value

