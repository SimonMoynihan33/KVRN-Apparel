from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from allauth.account.models import EmailAddress
from .models import CustomUser


def verify_email(modeladmin, request, queryset):
    """
    Custom admin action to mark selected users' emails as verified.

    For each selected user, finds the associated email address and sets
    it as verified, then saves the updated status.
    """
    for user in queryset:
        email_address = EmailAddress.objects.filter(user=user).first()
        if email_address:
            email_address.verified = True
            email_address.save()


verify_email.short_description = "Mark selected users as email verified"


class CustomUserAdmin(UserAdmin):
    """
    Custom admin class for managing CustomUser instances.

    Displays user details including username, email, and email verification
    status.Includes a custom action to mark emails as verified and a read-only
    field showing the verification status.
    """

    list_display = ("username", "email", "is_email_verified")
    readonly_fields = ("is_email_verified",)
    actions = [verify_email]

    def is_email_verified(self, obj):
        """Check if the user’s email is verified."""
        return obj.is_email_verified()

    is_email_verified.boolean = True
    is_email_verified.short_description = "Email Verified"


# Unregister the default User admin and register the CustomUser proxy
admin.site.unregister(User)
admin.site.register(CustomUser, CustomUserAdmin)
