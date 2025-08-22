from django.urls import path

from bookings.views import (
    BookingCreateView,
    BookingCancelView,
    MyBookingListView,
    ManageBookingsView,
)

app_name = "bookings"


urlpatterns = [
    path("book/<int:book_pk>/reserve/", BookingCreateView.as_view(), name="book-reserve"),
    path("reservation/<int:pk>/cancel/", BookingCancelView.as_view(), name="reservation-cancel"),
    path("my-reservations/", MyBookingListView.as_view(), name="my-reservations"),
    path("book-requests/", ManageBookingsView.as_view(), name="book-requests")
]