from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic


#request for reservation
class BookingCreateView(LoginRequiredMixin, generic.CreateView):
    pass

#cancel request for reservation
class BookingCancelView(LoginRequiredMixin, generic.View):
    pass


#My requests
class MyBookingListView(LoginRequiredMixin, generic.View):
    pass

#manage requests for my books
class ManageBookingsView(LoginRequiredMixin, generic.View):
    pass
