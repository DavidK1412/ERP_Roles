from functools import wraps
from django.core.exceptions import PermissionDenied

from authApp.utils import request_decode_token
from authApp.models import User
from securityApp.models import Permission, Role


def is_granted(*permission_names):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            token_user_id = request_decode_token(request)['user_id']
            user = User.objects.get(pk=token_user_id)
            if not user.is_authenticated:
                raise PermissionDenied('Usuario no autenticado')
            try:
                Permission.objects.filter(name__in=permission_names)
            except Permission.DoesNotExist:
                raise PermissionDenied('Permiso no encontrado')

            if user.user_permissions.filter(name__in=permission_names).exists():
                return view_func(request, *args, **kwargs)

            user_roles = Role.objects.filter(users=user)
            for role in user_roles:
                if role.permissions.filter(name__in=permission_names).exists():
                    return view_func(request, *args, **kwargs)

            raise PermissionDenied('Permisos insuficientes')
        return _wrapped_view
    return decorator
