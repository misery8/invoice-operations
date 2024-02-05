from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

User = get_user_model()


class UserUpdateView(LoginRequiredMixin, UpdateView):

    model = User
    form_class = UserChangeForm
    template_name = 'accounts/profile.html'
    success_url = reverse_lazy('index')
