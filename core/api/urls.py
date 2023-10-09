from django.urls import path

from .views import ItemListAPIView

app_name = 'api'


urlpatterns = [
    path('items/', ItemListAPIView.as_view(), name='items')
]