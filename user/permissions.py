from rest_framework.permissions import BasePermission

class SignupPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action == 'signup':
            return True
        return request.user and request.user.is_authenticated