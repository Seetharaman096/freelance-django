from django.contrib import admin
from .models import ContactMessage

# Register your models here.
@admin.register(ContactMessage)
class ContactMessage(admin.ModelAdmin):
    list_display = ['name', 'email','service', 'budget', 'created_at', 'is_read']
    list_filter = ['is_read', 'service', 'created_at']
    search_fields = ['name', 'email', 'message']
    readonly_fields = ['name', 'email', 'service', 'other_service', 
                       'budget', 'message', 'created_at']
    ordering = ['-created_at']
    
    actions = ['mark_as_read']

    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = "Mark selected messages as read"

    