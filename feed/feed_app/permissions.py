from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsSubscriber(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and not request.user.is_anonymous)

class IsAuthorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(request.method in SAFE_METHODS or request.user and not request.user.is_anonymous and request.user.is_author)

class IsAuthor(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and not request.user.is_anonymous and request.user.is_author)