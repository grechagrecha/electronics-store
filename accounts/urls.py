from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/<int:user_id>', views.ProfileView.as_view(), name='profile'),
]
