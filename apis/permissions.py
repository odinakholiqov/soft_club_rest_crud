from rest_framework.permissions import BasePermission


class IsAuthorOrReadOnly(BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.user == obj.author:
            return True
        elif request.user.is_authenticated:
            if request.method not in ('GET', 'HEAD', 'OPTIONS'):
                return False
            else:
                return True
            
        else:
            return False