from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import User, Profile


@admin.register(User)
class UserAdmin(UserAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "phone", "city", "country", "is_public", "created_at")
    list_filter = ("country", "is_public", "created_at")
    search_fields = ("user__username", "city", "country")
    ordering = ("-created_at",)