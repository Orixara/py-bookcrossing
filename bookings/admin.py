from django.contrib import admin

from bookings.models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "borrower",
        "book",
        "status",
        "booked_at",
        "deadline",
        "returned_at"
    )

    list_filter = ("status", "booked_at", "deadline")
    search_fields = ("borrower__username", "book__title", "book__author__full_name")
    ordering = ("-booked_at",)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ("booked_at",)
        else:
            return ("booked_at", "returned_at")

    fieldsets = (
        ("Main Information", {
            "fields": ("book", "borrower", "status")
        }),
        ("Time Frames", {
            "fields": ("booked_at", "deadline", "returned_at")
        }),
    )
