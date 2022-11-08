from django.contrib import admin

from accounts.models import User,Role,Permissions

# Register your models here.

admin.site.register(User)
admin.site.register(Role)
admin.site.register(Permissions)


