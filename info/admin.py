from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'submitted_at')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('submitted_at',)  # Filter by submission date
    readonly_fields = ('submitted_at',)

    # Optional: Customize how the form appears in the admin detail view
    fieldsets = (
        (None, {
            'fields': ('name', 'email', 'subject', 'message', 'submitted_at')
        }),
    )
