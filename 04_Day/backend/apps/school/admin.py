from django.contrib import admin
from .models import School


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug", "created_at")
    search_fields = ("name", "address")
    list_display_links = ("name",)
    readonly_fields = ("created_at", "slug")

    list_filter = ("created_at",)

    # Automatically fills slug when typing in admin
    prepopulated_fields = {"slug": ("name",)}
