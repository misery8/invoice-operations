from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

User = get_user_model()


class UserCreateView(CreateView):

    form_class = UserCreationForm
    model = User
    template_name = 'registration/sign-up.html'
    success_url = reverse_lazy('index')
