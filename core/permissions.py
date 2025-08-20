from rest_framework.permissions import BasePermission

class IsAdminOrTeacher(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role in ("ADMIN", "TEACHER"))

class AdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return bool(request.user and request.user.is_authenticated and request.user.role == "ADMIN")