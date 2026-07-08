from rest_framework import permissions

 #Only the use who have created the Post can edit or update the post
class IsPostPosessor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        #only reading for others no delete or update
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.created_by == request.user
