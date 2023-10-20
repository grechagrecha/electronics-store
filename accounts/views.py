from django.views.generic import TemplateView, CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ProfileView(TemplateView):
    model = User
    context_object_name = 'user'
    template_name = 'accounts/profile.html'


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = '/accounts/login'
