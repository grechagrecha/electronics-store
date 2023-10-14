from django.views.generic import TemplateView
from django.contrib.auth.models import User


class ProfileView(TemplateView):
    model = User
    context_object_name = 'user'
    template_name = 'accounts/profile.html'
