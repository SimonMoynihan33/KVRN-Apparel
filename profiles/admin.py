from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, User
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_email_verified')
    readonly_fields = ('is_email_verified',)

    def is_email_verified(self, obj):
        """Check if the user’s email is verified."""
        return obj.is_email_verified()
    is_email_verified.boolean = True  # Display as a boolean (checkbox)
    is_email_verified.short_description = 'Email Verified'


# Unregister the default User admin and register the CustomUser proxy
admin.site.unregister(User)
admin.site.register(CustomUser, CustomUserAdmin)
