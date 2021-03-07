from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allows the users to edit their profiles only"""

    def has_object_permission(self, request, view, obj):
        """Check if user is trying to edit their profile only or not"""

        # if method is HTTP get or POST, it is safe, so we set to True to allow it
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id

class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to update their own status"""
    #Ensure the user is updating the status that is assigned to their account only

    def has_object_permission(self, request, view, obj):
        """check if user is trying to update their status"""

        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_profile.id == request.user.id
