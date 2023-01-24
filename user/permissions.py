from rest_framework.permissions import BasePermission

class IsAllowedToSignup(BasePermission):
    def has_permission(self, request, view):
        # check if the user is allowed to signup
        return request.user.is_authenticated and request.user.is_active