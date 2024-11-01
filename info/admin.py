from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Read-only admin interface allows store owners to view messages
    submitted by users through the contact form.
    """
    list_display = ('name', 'email', 'subject', 'submitted_at')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('submitted_at',)  # Filter by submission date
    readonly_fields = ('name', 'email', 'subject', 'message', 'submitted_at')

    # Optional: Customize how the form appears in the admin detail view
    fieldsets = (
        (None, {
            'fields': ('name', 'email', 'subject', 'message', 'submitted_at')
        }),
    )
