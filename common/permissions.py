from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    """
    Custom permission to allow only the owner of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request (GET, HEAD, OPTIONS)
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # Write permissions (e.g., PUT, PATCH, DELETE) are only allowed to the owner of the object
        return obj.owner == request.user or request.user.is_staff
