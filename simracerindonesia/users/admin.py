from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from reversion.admin import VersionAdmin

from .models import User, UserProfile


@admin.register(User)
class MyUserAdmin(VersionAdmin, AuthUserAdmin):
    fieldsets = (
                    ('User Profile', {'fields': ('name',)}),
                ) + AuthUserAdmin.fieldsets
    list_display = ('username', 'name', 'email', 'is_superuser')
    search_fields = ['name', 'email']


@admin.register(UserProfile)
class UserProfileAdmin(VersionAdmin):
    search_fields = ['user__username']
    exclude = ('created_date', 'update_date')
    list_display = ('user',)
