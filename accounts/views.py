from django.views.generic import TemplateView


class ProfileView(TemplateView):
    model = None
    template_name = 'accounts/profile.html'
