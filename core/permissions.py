from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'admin'

class IsDean(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'dean'

class IsAdviser(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'adviser'

class IsOrganization(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'organization'
