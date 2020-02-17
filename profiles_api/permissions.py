from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """allow users to edit only their own profile """

    def has_object_permission(self, request, view, obj):
        """check user is trying to edit their own profile """
        if request.method in permissions.SAFE_METHODS:  # this allows only the user of their own profile to update
            # their own profile
            return True

        return obj.id == request.user.id


# users can only update there own status
class UpdateOwnStatus(permissions.BasePermission):
    """Allows users to update their own staus """

    def has_object_permission(self, request, view, obj):
        """check the user is trying to update their own status """
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
