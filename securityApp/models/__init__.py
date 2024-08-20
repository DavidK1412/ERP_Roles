from django.contrib import admin
from .role import Role
from .permission import Permission
from .module import Module

admin.site.register(Role)
admin.site.register(Permission)
admin.site.register(Module)
