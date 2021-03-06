from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allows the users to edit their profiles only"""

    def has_object_permission(self, request, view, obj):
        """Check if user is trying to edit their profile only or not"""

        # if method is HTTP get, it is safe, so we set to True to allow it
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
