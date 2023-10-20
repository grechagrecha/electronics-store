from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('profile/<int:user_id>', views.ProfileView.as_view(), name='profile'),
]
