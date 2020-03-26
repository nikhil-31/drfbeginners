from rest_framework import permissions


class IsOwnerPermission(permissions.BasePermission):

    # Checks if the user making the call is the user that created it
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
