from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Booking(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = "pending", "Pending"
        ACTIVE = "active", "Active"
        COMPLETED = "completed", "Completed"
        CANCELLED = "cancelled", "Cancelled"

    book = models.ForeignKey(
        "books.BookListing",
        related_name="bookings",
        on_delete=models.CASCADE
    )
    borrower = models.ForeignKey(
        User,
        related_name="bookings",
        on_delete=models.CASCADE
    )
    booked_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    returned_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.PENDING
    )


    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"
        ordering = ["-booked_at"]

    def __str__(self):
        return f"Booking: {self.borrower.username} - {self.book.title}"
