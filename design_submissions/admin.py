from django.contrib import admin
from .models import UserDesignSubmission


class UserDesignSubmissionAdmin(admin.ModelAdmin):
    """
    Admin configuration for UserDesignSubmission model.

    This admin class allows easy management of user design submissions,
    including displaying relevant fields, filtering by status and creation
    date, and performing bulk actions to mark submissions as processed.
    """

    list_display = ("title", "user", "status", "created_at", "updated_at")
    list_filter = ("status", "created_at")
    search_fields = ("title", "user__username", "description")
    actions = ["mark_as_processed"]

    # Custom action to mark submissions as processed
    def mark_as_processed(self, request, queryset):
        queryset.update(status="processed")
        self.message_user(
            request, "Selected submissions have been marked as processed."
        )

    mark_as_processed.short_description = "Mark selected submissions as \
        processed"


admin.site.register(UserDesignSubmission, UserDesignSubmissionAdmin)
