from rest_framework.permissions import BasePermission

class IsNormalUser(BasePermission):
    def has_permission(self, request, view):
        return not (request.user.is_staff or request.user.is_artist or request.user.is_superuser)

class IsArtist(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_artist

class IsStaff(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff 

class IsSuperuser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser and request.user.is_staff 

class IsBand(BasePermission):
    def has_permission(self, request, view):
        return False
    
class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
