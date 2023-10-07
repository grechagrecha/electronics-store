from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from store.settings.settings import MEDIA_URL, MEDIA_ROOT, STATIC_URL, STATIC_ROOT

app_name = 'store'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('accounts/', include('accounts.urls')),
]

urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
