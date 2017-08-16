from rest_framework import permissions


class IsAdminOrMentor(permissions.BasePermission):
    """
    If you are candidate, you are denied
    """
    message = "Candidate doesn't have access"

    def has_permission(self, request, view):
        if request.user.user_type == 'C':
            return False
        return True
