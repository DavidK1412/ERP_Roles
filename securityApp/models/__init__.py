from django.contrib import admin
from .role import Role
from .permission import Permission

admin.site.register(Role)
admin.site.register(Permission)
