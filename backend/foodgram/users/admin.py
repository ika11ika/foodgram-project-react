from django.contrib import admin

from .models import Follow, User


class UserAdmin(admin.ModelAdmin):
    list_filter = ('login', 'email')


admin.site.register(Follow)
admin.site.register(User, UserAdmin)
