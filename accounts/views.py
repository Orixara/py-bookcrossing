from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic


#custom registration
class SignUpView(generic.CreateView):
    pass


#email activation
class ActivateAccountView(generic.View):
    pass


#check profile
class ProfileView(LoginRequiredMixin, generic.DetailView):
    pass


#edit your profile
class ProfileUpdateView(LoginRequiredMixin, generic.UpdateView):
    pass