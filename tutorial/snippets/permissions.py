from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    @description: 自定义权限：只允许snippets的拥有者去编辑snippets
    """
    def has_object_permission(self, request, view, obj):
        #任何请求都有读的权限
        #允许GET, HEAD 或选择的请求
        if request.method in permissions.SAFE_METHODS:
            return True

        #只有snippets的拥有者有写权限
        return obj.owner == request.user